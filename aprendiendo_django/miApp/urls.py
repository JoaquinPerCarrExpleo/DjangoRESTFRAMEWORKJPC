#from django.contrib import admin
from django.urls import path
#from . import views
from miApp.api.views import ProjectListAPI

urlpatterns = [
    path('',ProjectListAPI.as_view()),
]