from django import urls
from django.urls import path
from . import views

app_name = "display"
urlpatterns = [
    path("", views.index, name="index"),
    path("staff", views.staff, name="staff"),
    path("user", views.user, name="user"),
    path("login", views.mylogin, name="login"),
    path("logout", views.mylogout, name="logout")
]
