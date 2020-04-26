from django.contrib import admin
from django.urls import path, include
from app_donate import views

urlpatterns = [
    path('', views.donate),
]