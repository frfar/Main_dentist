from django.contrib import admin
from django.urls import path
from . import views


app_name = "mainapp"
urlpatterns = [
    path('', views.home, name='home'),
    path('About/', views.about, name='about'),
    path('Service/', views.service, name='service'),
    path('Service/<slug:slug>', views.service_detail, name='service_detail'),
    path('Patients/', views.patients, name='patients'),
    path('Testimonials/', views.testimonials, name='testimonials'),
    path('Contact/', views.contact, name='contact'),
    path('send_email/', views.sendEmail, name='send_email'),
]
