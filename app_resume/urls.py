from django.contrib import admin
from django.urls import path, include
from app_resume import views

urlpatterns = [
    path('', views.resumepage),
]