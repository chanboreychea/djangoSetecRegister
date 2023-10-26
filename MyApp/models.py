import os
from datetime import datetime
from django.utils import timezone

from django.db import models

def UniqueFilename(instance, filename):
    timestamp = timezone.now()
    filename, file_extension = os.path.splitext(filename)
    return f'media/{timestamp:%Y-%m-%d-%H-%M-%S}{file_extension}'


class Users(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phoneNumber = models.CharField(max_length=20)
    password = models.CharField()
    address = models.CharField(max_length=255)
    dateOfBirth = models.DateField()
    gender = models.CharField(max_length=1)
    img = models.ImageField(upload_to=UniqueFilename)
    createAt = models.DateTimeField(auto_now_add=datetime.now())


class Register(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    # registerType = models.CharField(max_length=1)
    # identifyType = models.CharField(max_length=1)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=100,unique=True)
    email = models.CharField(max_length=100,unique=True)
    address = models.CharField(max_length=255)
    dateOfBirth = models.DateField()
    gender = models.CharField(max_length=1)
    img = models.ImageField(upload_to=UniqueFilename)
    emergencyContactName = models.CharField(max_length=100, null=True, blank=True)
    emergencyPhoneNumber = models.CharField(max_length=100, null=True, blank=True)
    emergencyAddress = models.CharField(max_length=100, null=True, blank=True)
    emergencyContactRelationship = models.CharField(max_length=100, null=True, blank=True)

    hightSchoolName = models.CharField(max_length=100, null=True)
    gratuationYear = models.CharField(max_length=100, null=True)
    grade = models.CharField(max_length=10, null=True)
    totalScore = models.FloatField(max_length=255, null=True)
    examCenter = models.CharField(max_length=100, null=True)
    seat = models.CharField(max_length=20, null=True)
    dateOfExamination = models.DateField(null=True)

    # countryName = models.CharField(max_length=100)
    # hightSchoolDiploma = models.ImageField(upload_to="media/", null=True)
    # hightSchoolTranscript = models.ImageField(upload_to="media/", null=True)

    # collegeName = models.CharField(max_length=100, null=True)
    # major = models.CharField(max_length=100, null=True)
    # credit = models.ImageField(upload_to="media/", null=True)
    # startDate = models.DateField(null=True)
    # endDate = models.DateField(null=True)

    examCertificate = models.ImageField(upload_to=UniqueFilename, null=True)
    # englishProficiency = models.ImageField(upload_to="media/", null=True)
    associateDegree = models.ImageField(upload_to=UniqueFilename, null=True)

    majorReference = models.CharField(max_length=100, null=True)

    createAt = models.DateField(auto_now_add=datetime.now())
    updateAt = models.DateField(null=True)

