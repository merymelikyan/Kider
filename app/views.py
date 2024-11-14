from django.shortcuts import render

from .models import (
    HeaderText,
    FooterText,
    Facilities,
    FacilityMain,
    MainSaction,
    AboutUs,
    AboutImages,
    Teacher,
    ClassesMain,
    Classes,
    Appointment,
    TeamMain,
    TeamBlocks,
    Testimonials,
    TestimonialsBlocks,
    Error,
    ContactUsMain,
    ContactBlocks,
    FooterMain,
    GetInTouch,
    Socials,
    QuickLinks,
    Newsletter,
    GalleryImages
   )


def index(request):
    context = {
        "header_text": HeaderText.objects.all(),
        "footer_text": FooterText.objects.all().first(),
        "facilities": Facilities.objects.all(),
        "facility_main": FacilityMain.objects.all().first(),
        "main_saction": MainSaction.objects.all().first(),
        "about_us": AboutUs.objects.all().first(),
        "about_images": AboutImages.objects.all(),
        "teacher": Teacher.objects.all().first(),
        "classes_main": ClassesMain.objects.all().first(),
        "classes": Classes.objects.all(),
        "appointment": Appointment.objects.all().first(),
        "team_main": TeamMain.objects.all().first(),
        "team_blocks": TeamBlocks.objects.all(),
        "testimonials": Testimonials.objects.all().first(),
        "testimonials_blocks": TestimonialsBlocks.objects.all(),
        "footer_main": FooterMain.objects.all(),
        "get_in_touch": GetInTouch.objects.all(),
        "socials": Socials.objects.all(),
        "quick_links": QuickLinks.objects.all(),
        "news_letter": Newsletter.objects.all().first(),
        "gallery": GalleryImages.objects.all()
    } 
    
    return render(request,"home.html", context)


def about(request):
    context = {
        "footer_text": FooterText.objects.all().first(),
        "about_us": AboutUs.objects.all().first(),
        "about_images": AboutImages.objects.all(),
        "teacher": Teacher.objects.all().first(),
        "team_main": TeamMain.objects.all().first(),
        "team_blocks": TeamBlocks.objects.all(),
        "footer_main": FooterMain.objects.all(),
        "get_in_touch": GetInTouch.objects.all(),
        "socials": Socials.objects.all(),
        "quick_links": QuickLinks.objects.all(),
        "news_letter": Newsletter.objects.all().first(),
        "gallery": GalleryImages.objects.all()
    } 
    
    return render(request,"about.html", context)



def contact(request):
    context = {

        "footer_text": FooterText.objects.all().first(),
        "main_saction": MainSaction.objects.all().first(),
        "contact_us_main": ContactUsMain.objects.all().first(),
        "contact_blocks": ContactBlocks.objects.all(),
        "footer_main": FooterMain.objects.all(),
        "get_in_touch": GetInTouch.objects.all(),
        "socials": Socials.objects.all(),
        "quick_links": QuickLinks.objects.all(),
        "news_letter": Newsletter.objects.all().first(),
        "gallery": GalleryImages.objects.all()
    }

    return render(request,"contact.html",context)


def appointment(request):
    context = {
        "footer_text": FooterText.objects.all().first(),
        "appointment": Appointment.objects.all().first(),
        "footer_main": FooterMain.objects.all(),
        "get_in_touch": GetInTouch.objects.all(),
        "socials": Socials.objects.all(),
        "quick_links": QuickLinks.objects.all(),
        "news_letter": Newsletter.objects.all().first(),
        "gallery": GalleryImages.objects.all()
    } 

    return render(request,"appointment.html",context)


def teachers(request):
    context = {
        "footer_text": FooterText.objects.all().first(),
        "teacher": Teacher.objects.all().first(),
        "footer_main": FooterMain.objects.all(),
        "get_in_touch": GetInTouch.objects.all(),
        "socials": Socials.objects.all(),
        "quick_links": QuickLinks.objects.all(),
        "news_letter": Newsletter.objects.all().first(),
        "gallery": GalleryImages.objects.all()
    } 
   
    return render(request,"call_to_action.html",context)


def classes(request):
    context = {
        "footer_text": FooterText.objects.all().first(),
        "classes_main": ClassesMain.objects.all().first(),
        "classes": Classes.objects.all(),
        "appointment": Appointment.objects.all().first(),
        "testimonials": Testimonials.objects.all().first(),
        "testimonials_blocks": TestimonialsBlocks.objects.all(),
        "footer_main": FooterMain.objects.all(),
        "get_in_touch": GetInTouch.objects.all(),
        "socials": Socials.objects.all(),
        "quick_links": QuickLinks.objects.all(),
        "news_letter": Newsletter.objects.all().first(),
        "gallery": GalleryImages.objects.all()
    } 

    return render(request,"classes.html",context)


def facility(request):
    context = {
        "footer_text": FooterText.objects.all().first(),
        "facilities": Facilities.objects.all(),
        "facility_main": FacilityMain.objects.all().first(),
        "footer_main": FooterMain.objects.all(),
        "get_in_touch": GetInTouch.objects.all(),
        "socials": Socials.objects.all(),
        "quick_links": QuickLinks.objects.all(),
        "news_letter": Newsletter.objects.all().first(),
        "gallery": GalleryImages.objects.all()
    } 
    
    return render(request,"facility.html",context)


def team(request):
    context = {
        "footer_text": FooterText.objects.all().first(),
        "team_main": TeamMain.objects.all().first(),
        "team_blocks": TeamBlocks.objects.all(),
        "footer_main": FooterMain.objects.all(),
        "get_in_touch": GetInTouch.objects.all(),
        "socials": Socials.objects.all(),
        "quick_links": QuickLinks.objects.all(),
        "news_letter": Newsletter.objects.all().first(),
        "gallery": GalleryImages.objects.all()
    } 

    return render(request,"team.html",context)


def error(request):
    context = {
        "footer_text": FooterText.objects.all().first(),
        "error": Error.objects.all().first(),
        "footer_main": FooterMain.objects.all(),
        "get_in_touch": GetInTouch.objects.all(),
        "socials": Socials.objects.all(),
        "quick_links": QuickLinks.objects.all(),
        "news_letter": Newsletter.objects.all().first(),
        "gallery": GalleryImages.objects.all()
    }
    return render(request, "404.html",context)


def testimonial(request):
    context = {
        "footer_text": FooterText.objects.all().first(),
        "testimonials": Testimonials.objects.all().first(),
        "testimonials_blocks": TestimonialsBlocks.objects.all(),
        "footer_main": FooterMain.objects.all(),
        "get_in_touch": GetInTouch.objects.all(),
        "socials": Socials.objects.all(),
        "quick_links": QuickLinks.objects.all(),
        "news_letter": Newsletter.objects.all().first(),
        "gallery": GalleryImages.objects.all()
    } 

    return render(request,"testimonial.html",context)


