from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import redirect
import os

# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.decorators.http import require_GET, require_POST
from django.contrib.auth.decorators import login_required

from MyApp.models import Register

from MyApp.models import Users


def logins(request):
    return render(request, "login.html")


@require_POST
def login_view(request):
    try:
        if request.user.is_authenticated:
            return redirect("/registers/index")
        user = User()
        user.username = request.POST["username"]
        user.password = request.POST["password"]
        user1 = authenticate(username=user.username, password=user.password)
        if user1:
            login(request, user1)
            return redirect("/registers/index")
            
        else:
            return render(request, "login.html")
    except Exception as ex:
        print(ex)
    


def logout_view(request):
    logout(request)
    return render(request, "login.html")


@login_required(login_url="/admins")
def index(request):
    users = Users.objects.all().order_by("id")
    context = {"users": users}
    return render(request, "users/index.html", context)


@require_GET
def show(request, id):
    user = User.objects.get(id=id)
    context = {"user": user}
    return render(request, "users/show.html", context)


@require_GET
def edit(request, id):
    user = User.objects.get(id=id)
    context = {"user": user}
    return render(request, "users/edit.html", context)


@require_POST
def update(request, id):
    user = User.objects.get(id=id)
    user.firstName = request.POST["txtFirstName"]
    user.lastName = request.POST["txtLastName"]
    gender = request.POST["txtGender"]
    if gender == "Male":
        user.gender = "m"
    else:
        user.gender = "f"
    user.email = request.POST["txtEmail"]
    user.phoneNumber = request.POST["txtPhoneNumber"]
    user.dateOfBirth = request.POST["txtDateOfBirth"]

    if len(request.FILES) != 0:
        if user.img:
            os.remove(user.img.path)
        user.img = request.FILES["img"]

    user.save()

    return redirect("/users/index")


@require_GET
def create(request):
    return render(request, "users/create.html")
