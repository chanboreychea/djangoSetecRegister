import re
from django import forms
from MyApp.models import Register
from django.db.models import Q
from django.core.validators import RegexValidator
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError

img_message = "Invalid file extension. Please upload a file with one of the following extensions: jpg, jpeg, png."
img_extensions = ["jpg", "jpeg", "png"]


def phoneR(value):
    if Register.objects.filter(phoneNumber=value).exists():
        raise ValidationError(
            ("Phone Number has been already!"),
            params={"value": value},
        )


def emailR(value):
    if Register.objects.filter(email=value).exists():
        raise ValidationError(
            ("Email has been already!"),
            params={"value": value},
        )


class RegisterForm(forms.Form):
    fname = forms.CharField(max_length=100)
    lname = forms.CharField(max_length=100)
    birthday = forms.DateField()
    phoneNumber = forms.CharField(
        max_length=13,
        validators=[
            RegexValidator(
                regex=r"^(0|\+855){1}\d{2}\d{6,7}$", message="(+855)|X XX XXX XXX"
            ),
            phoneR,
        ],
    )
    email = forms.EmailField(validators=[emailR])
    address = forms.CharField(max_length=255)

    highSchool = forms.CharField(max_length=100)
    graduationYear = forms.CharField(max_length=4)
    examGrade = forms.CharField(max_length=10)
    examTotalScore = forms.CharField(max_length=255)
    examCenter = forms.CharField(max_length=100)
    seat = forms.CharField(max_length=20)
    examDate = forms.DateField()

    image = forms.ImageField(
        validators=[
            FileExtensionValidator(
                allowed_extensions=img_extensions, message=img_message
            ),
        ]
    )
    examResult = forms.ImageField(
        validators=[
            FileExtensionValidator(
                allowed_extensions=img_extensions, message=img_message
            ),
        ]
    )
    associateDegree = forms.ImageField(
        validators=[
            FileExtensionValidator(
                allowed_extensions=img_extensions, message=img_message
            ),
        ]
    )


class UpdateRegister(forms.Form):
    id = forms.IntegerField()
    fname = forms.CharField(max_length=100)
    lname = forms.CharField(max_length=100)
    birthday = forms.DateField()
    phoneNumber = forms.CharField(
        max_length=13,
        validators=[
            RegexValidator(
                regex=r"^(0|\+855){1}\d{2}\d{6,7}$", message="(+855)|X XX XXX XXX"
            ),
        ],
    )
    email = forms.EmailField()
    address = forms.CharField(max_length=255)
    highSchool = forms.CharField(max_length=100)
    graduationYear = forms.CharField(max_length=4)
    examGrade = forms.CharField(max_length=10)
    examTotalScore = forms.CharField(max_length=255)
    examCenter = forms.CharField(max_length=100)
    seat = forms.CharField(max_length=20)
    examDate = forms.DateField()

    def clean_phoneNumber(self):
        idd = self.cleaned_data.get("id")
        phone = self.cleaned_data.get("phoneNumber")
        if Register.objects.exclude(id=idd).filter(phoneNumber=phone):
            raise forms.ValidationError("Phone Number has been already!")
        return phone

    def clean_email(self):
        idd = self.cleaned_data.get("id")
        em = self.cleaned_data.get("email")
        if Register.objects.exclude(id=idd).filter(email=em):
            raise forms.ValidationError("Email has been already!")
        return em
