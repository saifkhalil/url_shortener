from django.contrib import admin
from .models import Shortener

# Register your models here.
class ShortenerAdmin(admin.ModelAdmin):
    list_display = ['short_url','times_followed','created']

admin.site.register(Shortener, ShortenerAdmin)