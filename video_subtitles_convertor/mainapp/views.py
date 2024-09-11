from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from .models import Video
from .forms import UploadVideoForm

# Create your views here.


class UploadVideo(CreateView):
    
    def __init__(self):
        
        print("CLass called")
        
    template_name = "mainapp/upload-video.html"
    form_class = UploadVideoForm
    success_url = reverse_lazy("authapp:list-videos")
    
    
class ListVideos(ListView):
    
    template_name="mainapp/list-video.html"
    model = Video
    
