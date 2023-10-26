"""
URL configuration for Mydemo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from MyApp import views
from MyApp.controllers import user_view, register_view

urlpatterns = [
    path("", views.homepage, name="/"),
    path("registers/store", views.store),
    
    path("admins", user_view.logins),
    path("logins", user_view.login_view),
    path("logouts", user_view.logout_view),
    
    path("registers/index", register_view.index),
    path("registers/show/<id>", register_view.show),
    path("registers/edit/<id>", register_view.edit),
    path("registers/update/<id>", register_view.update),
    path("registers/destroy/<id>", register_view.destroy),
    # users
    path("users/index", user_view.index),
    path("users/show/<id>", user_view.show),
    path("users/edit/<id>", user_view.edit),
    path("users/update/<id>", user_view.update),
    path("users/create", user_view.create),
]
