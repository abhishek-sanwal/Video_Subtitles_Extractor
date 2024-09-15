from django.contrib import admin

# Register your models here.

from .models import Video,Subtitles

# So that these models will show in admin panel
admin.site.register(Video)
admin.site.register(Subtitles)