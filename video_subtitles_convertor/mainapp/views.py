

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, View
from django.shortcuts import redirect


from .models import Video
from .forms import UploadVideoForm
from .NoSubtitlesException import NoSubtitlesException

# ffmpeg command  =>
# ffmpeg -i test1.webm -map 0:5 -c:s  srt output_subtitles.srt

import subprocess
import uuid
from typing import List

subtitle_language_codes: List[str] = [
    "hin", "ger", "kor",
    "eng", "chi", "spa",
    "fre", "ara", "por",
    "rus", "bra"
]


# Check streams available for Input Video File
def checkSubtitlesStreams(input_file: str) -> str:

    # ffmpeg command to extract various available streams for Input Video File
    command: str = f"ffmpeg -i {input_file[1:]}"

    # Will store the command_output
    cmd_output: str = ""
    
    try:
        cmd_output = subprocess.run(
            command, capture_output=True,
            shell=True, text=True)

    except Exception as e:

        print(e)
    # print(cmd_output.stderr)
    return cmd_output.stderr


# Check all available subtiltes streams and choose the first
def getAvailableSubtitles(cmd_output: str) -> str:

    # Get each line of output
    streamCode: str = ""

    for line in cmd_output.split("\n"):
        # Fetch each word from line
        word: List[str] = line.strip().split()

        # We are using first subtitles track to put it on video
        # fetch first subtitles track from file
        if word and word[0] == "Stream" and word.count("(srt)") > 0:

            print("stremCode", word[1][1:4])
            streamCode: str = word[1][1:4]

            break

    return streamCode


def convertToSrt(input_file: str, stream_code: str) -> str:
    
    filename = input_file.split("/")[3]
    
    # If no subtitles track is available raise error
    if not stream_code:

        print("Operation Failed !.NO Available Subtitles track for this Video.")
        raise NoSubtitlesException(
            "No Available Subtitles Track available for Video")

    # Output subtitle file location and name
    output_fileName = f"assets/subtitles/{filename}_subs.srt"
    
    command = f"ffmpeg -i {input_file[1:]} -map {stream_code} {output_fileName}"

    try:
        subprocess.run(
            command, capture_output=True, shell=True, text=True)

    except Exception as e:
        print(e)

    return output_fileName


# Save subtitles into db for Searching purposes
def saveSubtitlesDb(video_id: int, subtitles_fileName: str) -> bool:

    pass


# Embed first subttitles track found into videos
def encodeVideoSubtitles(input_file: str, subtitles_fileName: str) -> str:

    print("Inside function")
    filename = input_file.split("/")[3]
    output_file = f"assets/output_videos/output_{filename}"
    command = f"ffmpeg -i {input_file[1:]} -vf subtitles={subtitles_fileName} {output_file}"

    try:
        output = subprocess.run(command, capture_output=True, shell=True, text=True)

    except Exception as e:
        print(e)
    print(output.stdout, output.stderr,"Message")
    return filename


def getVideoUrl(video_id):

    data = Video.objects.filter(video_id__iexact=video_id)

    if not data:
        return ""

    return data.first().video_file.url


class UploadVideo(View):

    def post(self, request):

        form = UploadVideoForm(request.POST, request.FILES)

        if form.is_valid():
            # uploaded_file = form["video_file"]
            instance = form.save(commit=False)
            video_id = uuid.uuid4()
            instance.video_id = video_id
            form.save()
            url = getVideoUrl(video_id)
            cmd_output = checkSubtitlesStreams(url)
            streamCode = getAvailableSubtitles(cmd_output)
            subtitles_filename = convertToSrt(url, streamCode)
            print(encodeVideoSubtitles(url,subtitles_filename))
            # saveSubtitlesDb(video_id ,fileName = "subs.srt")
            return redirect("mainapp:list-videos")

    def get(self, request):

        form = UploadVideoForm()
        return render(request, template_name="mainapp/upload-video.html", context={
            "form": form
        })


class ListVideos(ListView):

    template_name = "mainapp/list-video.html"
    model = Video
