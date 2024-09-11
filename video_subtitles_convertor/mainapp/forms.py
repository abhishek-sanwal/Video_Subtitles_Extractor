

from .models import Video
from django import forms

class UploadVideoForm(forms.ModelForm):
    
    class Meta:
        
        model  = Video
        fields = ["video_name","video_file"]