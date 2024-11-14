from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name = "index"),   
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('appointment/', views.appointment, name="appointment"),
    path('teachers/', views.teachers, name="teachers"),
    path('classes/', views.classes, name="classes"),   
    path('facility/', views.facility, name="facility"),
    path('team/', views.team, name="team"),
    path('testimonial/', views.testimonial, name="testimonial"),
    path('error/', views.error, name="error"),
    
] 