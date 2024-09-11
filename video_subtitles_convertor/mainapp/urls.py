
from django.urls import path

from .views import UploadVideo, ListVideos

app_name = "authapp"

urlpatterns = [
    path("upload-video", UploadVideo.as_view(), name="upload-video"),
    path("list-videos", ListVideos.as_view(),name="list-videos")
]
