"""
virtualmind URLs

"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include("restapi.urls")),
    path('admin/', admin.site.urls),
]
