"""
virtualmind - URLs

"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("mult/<str:args>/", views.helloworld, name="helloworld"),
]
