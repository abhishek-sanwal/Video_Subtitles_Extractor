
from django.urls import path

from .views import UploadVideoView, ListVideos, SubtitlesDetails

# App namespace
app_name = "mainapp"

urlpatterns = [
    path("upload-video", UploadVideoView.as_view(), name="upload-video"),
    path("list-videos", ListVideos.as_view(), name="list-videos"),
    path("search-subtitles",SubtitlesDetails.as_view(),name="search-subtitles")
]
