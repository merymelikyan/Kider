from django.contrib import admin

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

admin.site.register(HeaderText)
admin.site.register(FooterText)
admin.site.register(FacilityMain)
admin.site.register(Facilities)
admin.site.register(MainSaction)
admin.site.register(AboutUs)
admin.site.register(AboutImages)
admin.site.register(Teacher)
admin.site.register(ClassesMain)
admin.site.register(Classes)
admin.site.register(Appointment)
admin.site.register(TeamMain)
admin.site.register(TeamBlocks)
admin.site.register(Testimonials)
admin.site.register(TestimonialsBlocks)
admin.site.register(Error)
admin.site.register(ContactUsMain)
admin.site.register(ContactBlocks)
admin.site.register(FooterMain)
admin.site.register(GetInTouch)
admin.site.register(Socials)
admin.site.register(QuickLinks)
admin.site.register(Newsletter)
admin.site.register(GalleryImages)