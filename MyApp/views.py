from django.shortcuts import redirect, render

from MyApp.forms import RegisterForm
from MyApp.models import Register
from django.views.decorators.http import require_GET, require_POST


def homepage(request):
    return render(request, "cambodian.html")


@require_POST
def store(request):
    form = RegisterForm(request.POST, request.FILES)
    if form.is_valid():
        register = Register()
        register.user_id = 3
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

        if len(request.FILES) != 0:
            register.examCertificate = request.FILES["examResult"]
            register.associateDegree = request.FILES["associateDegree"]
            register.img = request.FILES["image"]

        register.majorReference = request.POST["radio"]

        register.save()

        return redirect("/")

    return render(request, "cambodian.html", {"form": form})
