from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import redirect
import os

# Create your views here.
from MyApp.forms import RegisterForm
from MyApp.models import Register
from django.views.decorators.http import require_GET, require_POST
from django.contrib.auth.decorators import login_required


@login_required(login_url="/admins")
def index(request):
    registers = Register.objects.all().order_by("id")
    context = {"registers": registers}
    return render(request, "registers/index.html", context)


@require_GET
def show(request, id):
    register = Register.objects.get(id=id)
    context = {"register": register}
    return render(request, "registers/show.html", context)


@require_GET
def edit(request, id):
    register = Register.objects.get(id=id)
    context = {"register": register}
    return render(request, "registers/edit.html", context)


@require_POST
def update(request, id):
    register = Register.objects.get(id=id)
    register.firstName = request.POST["fname"]
    register.lastName = request.POST["lname"]
    register.gender = request.POST["gender"]
    register.dateOfBirth = request.POST["birthday"]
    register.phoneNumber = request.POST["phoneNumber"]
    register.email = request.POST["email"]
    register.address = request.POST["address"]

    register.emergencyContactName = request.POST["eContactName"]
    register.emergencyPhoneNumber = request.POST["eContactPhoneNumber"]
    register.emergencyAddress = request.POST["eAddress"]
    register.emergencyContactRelationship = request.POST["eCRationship"]

    register.hightSchoolName = request.POST["highSchool"]
    register.gratuationYear = request.POST["graduationYear"]
    register.grade = request.POST["examGrade"]
    register.totalScore = request.POST["examTotalScore"]
    register.dateOfExamination = request.POST["examDate"]
    register.seat = request.POST["seat"]
    register.examCenter = request.POST["examCenter"]

    if request.FILES.getlist("image"):
        if register.img:
            os.remove(register.img.path)
        register.img = request.FILES["image"]
    

    if request.FILES.getlist("examResult"):
        if register.examCertificate:
            os.remove(register.examCertificate.path)
        register.img = request.FILES["examResult"]
    

    if request.FILES.getlist("associateDegree"):
        if register.associateDegree:
            os.remove(register.associateDegree.path)
        register.associateDegree = request.FILES["associateDegree"]
    

    register.majorReference = request.POST["radio"]

    register.save()

    return redirect("/registers/index")


@require_GET
def destroy(request, id):
    register = Register.objects.get(id=id)
    if register.img:
        os.remove(register.img.path)
    if register.examCertificate:
        os.remove(register.examCertificate.path)
    if register.associateDegree:
        os.remove(register.associateDegree.path)

    register.delete()
    return redirect("/registers/index")
