from django.contrib import admin
from django.contrib.admin import register

from shortener.models import URL


@register(URL)
class URLAdmin(admin.ModelAdmin):
    list_display = ['session', 'url', 'short_url', 'created', ]
