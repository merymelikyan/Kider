from django.shortcuts import render

from .models import (
    HeaderText,
    FooterText
   )


def index(request):
    context = {
        "header_text": HeaderText.objects.all(),
        "footer_text": FooterText.objects.all().first(),
    } 
    
    return render(request,"home.html", context)


def about(request):
    
    return render(request,"about.html")


def contact(request):
    
    return render(request,"contact.html")


def appointment(request):
    
    return render(request,"appointment.html")


def call_to_action(request):
    
    return render(request,"call_to_action.html")


def classes(request):
    
    return render(request,"classes.html")


def facility(request):
    
    return render(request,"facility.html")


def team(request):
    
    return render(request,"team.html")


def error(request):
    
    return render(request, "404.html")


def testimonial(request):
    
    return render(request,"testimonial.html")


