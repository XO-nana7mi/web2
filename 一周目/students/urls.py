"""
URL configuration for students project.

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
from django.urls import path
from my_app import views

urlpatterns = [
    path("list_stu/add_stu/", views.stu_add),
    path("list_stu/add_score/", views.add_score),
    path("list_stu/add_tea/", views.add_tea),
    path("list_stu/add_cour/", views.add_cour),
    path("list_stu/", views.list_stu),
    path("look_score/", views.look_score),
    path("search/", views.search),
    path("login_/", views.login),
]
