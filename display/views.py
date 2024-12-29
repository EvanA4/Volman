from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpRequest
from django.contrib.auth import authenticate, login


# Create your views here.
app_name = "display"
def index(request: HttpRequest):
    return render(request, "index.html", {})

@login_required
def staff(request: HttpRequest):
    return render(request, "staff.html", {})

@login_required
def user(request: HttpRequest):
    return render(request, "user.html", {})

def mylogin(request: HttpRequest):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        return redirect("display:login")
    else:
        return render(request, "login.html")