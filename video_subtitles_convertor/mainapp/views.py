

from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import  ListView, View,FormView,vi
from django.shortcuts import redirect
from django.db.models import Q
from django.urls import reverse_lazy

from .models import Video, Subtitles
from .forms import UploadVideoForm
from .tasks import process_video
import uuid
from typing import List,Any


# Subtitles language codes provided by Ffmpeg(Fast forward multimedia)
subtitle_language_codes: List[str] = [
    "hin", "ger", "kor",
    "eng", "chi", "spa",
    "fre", "ara", "por",
    "rus", "bra"
]


# A helper function to get filePath
def getVideoUrl(video_id:str)->str:

    data = Video.objects.filter(video_id__iexact=video_id)

    if not data:
        return ""

    return data.first().video_file.url


# Upload video view
class UploadVideoView(FormView):

    template_name = "mainapp/upload-video.html"
    form_class = UploadVideoForm
    success_url = reverse_lazy("mainapp:list-videos")
    
    def form_valid(self, form: UploadVideoForm) -> HttpResponse:
        
        instance:UploadVideoForm = form.save(commit=False)
        video_id:int = uuid.uuid4()
        instance.video_id = video_id
        form.save()
        url:str = getVideoUrl(video_id)
        
        # Trigger celery task
        process_video.delay(url,video_id)
        # return response
        return super().form_valid(form)
        
# List all videos view
class ListVideos(ListView):

    template_name = "mainapp/list-video.html"
    model = Video
    paginate_by = 50
    context_object_name = "videos"
    

# Subtitles Search View
class SubtitlesDetails(ListView):
    
    template_name = "mainapp/list-subtitles.html"
    model = Subtitles
    context_object_name = "subtitles_list"
    
    # Filter results
    def get_queryset(self) -> QuerySet[Subtitles]:
        
        search_word = self.request.GET.get("search",None)
        print(search_word)
        result = None
        if search_word:
            # Case insensitive search
            result = Subtitles.objects.filter(word__iexact = search_word.lower())
        print(result)
        return result
        
        
        
