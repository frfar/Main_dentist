from django.contrib.auth import views
from django.contrib import admin
from django.urls import path
from . import views


app_name = 'account'
urlpatterns = [
    path('register/', views.registerPage , name="register"),
    path('login/', views.loginPage , name="login"),
    path('logout/', views.logoutUser , name="logout"),
]