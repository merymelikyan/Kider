from django.contrib import admin

from .models import (
    HeaderText,
    FooterText
   )

admin.site.register(HeaderText)
admin.site.register(FooterText)
