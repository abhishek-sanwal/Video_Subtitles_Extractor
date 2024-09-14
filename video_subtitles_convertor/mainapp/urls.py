
from django.urls import path

from .views import UploadVideo, ListVideos, SubtitlesDetails

app_name = "mainapp"

urlpatterns = [
    path("upload-video", UploadVideo.as_view(), name="upload-video"),
    path("list-videos", ListVideos.as_view(), name="list-videos"),
    path("search-subtitles",SubtitlesDetails.as_view(),name="search-subtitles")
]
