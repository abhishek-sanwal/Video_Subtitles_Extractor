from django.contrib import admin

# Register your models here.

from .models import Video,Subtitles

admin.site.register(Video)
admin.site.register(Subtitles)