from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse
from django.contrib.auth import authenticate, login, logout
from .models import Volunteer, Session
import json


# Create your views here.
app_name = "display"
def index(request: HttpRequest):
    return render(request, "index.html", { "user": request.user })

def staff(request: HttpRequest):
    if not request.user.is_authenticated or not request.user.is_staff:
        return redirect("display:login")
    
    # http://127.0.0.1:8000/staff?volname=Adam%20Craig
    volname = request.GET.get('volname', 'undefined')
    if volname != "undefined":
        vol = Volunteer.objects.get(name=volname)

        stringMe = {
            "vol": {
                "name": vol.name,
                "email": vol.email,
                "age": vol.age
            },
            "seshs": [],
            "num_seshs": 0,
            "total_hr": 0,
            "avg_hr": 0
        }

        seshs = vol.sessions.all()
        stringMe["num_seshs"] = len(seshs)
        for sesh in seshs:
            stringMe["total_hr"] += sesh.length
            stringMe["seshs"].append({
                "length": sesh.length,
                "beganAt": sesh.beganAt.strftime("%B %d, %Y %I:%M:%S %p")
            })
        stringMe["avg_hr"] = stringMe["total_hr"] / stringMe["num_seshs"] if len(seshs) else 0
        
        return HttpResponse(json.dumps(stringMe))

    return render(request, "staff.html", {
        "user": request.user,
        "vols": Volunteer.objects.all()
    })


def user(request: HttpRequest):
    if not request.user.is_authenticated:
        return redirect("display:login")
    
    try:
        vol = Volunteer.objects.get(email=request.user.email)
        seshs = vol.sessions.all()
        num_seshs = len(seshs)
        total_hr = 0
        for sesh in seshs:
            total_hr += sesh.length
        avg_hr = total_hr / num_seshs

        return render(request, "user.html", {
            "user": request.user,
            "vol": vol,
            "seshs": seshs,
            "num_seshs": num_seshs,
            "total_hr": total_hr,
            "avg_hr": avg_hr
        })
    
    except:
        return redirect("display:login")

def mylogin(request: HttpRequest):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("display:index")
        return redirect("display:login")
    else:
        return render(request, "login.html")
    
def mylogout(request: HttpRequest):
    if request.user is not None:
        logout(request)
    return redirect("display:index")