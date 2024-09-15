
from celery import shared_task
from .models import Video, Subtitles
from .CustomException import NoSubtitlesException, VideoFileNotFoundException
from typing import List
import subprocess

# A  lambda function to remove specialcharacters and numbers 
# Case insensitive Search
removeOtherCharacters = lambda word:"".join([i.lower() for i in word if i.isalpha()])

# Subtitles language codes provided by Ffmpeg(Fast forward multimedia)
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
        # Run command
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

    # Process line-by-line
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

    # Fetch Input FileName
    filename:str = input_file.split("/")[3]

    # If no subtitles track is available raise error
    if not stream_code:

        print("Operation Failed !.NO Available Subtitles track for this Video.")
        raise NoSubtitlesException(
            "No Available Subtitles Track available for Video")

    # Output subtitle file location and name
    output_fileName = f"assets/subtitles/{filename}_subs.srt"

    command:str = f"ffmpeg -i {input_file[1:]} -map {stream_code} {output_fileName}"

    try:
        # Run command
        subprocess.run(
            command, capture_output=True, shell=True, text=True)

    except Exception as e:
        print(e)

    return output_fileName

# Parse SRT Files 
def parse_srt(subtitles_file:str)->str:

    # Read subtitles file
    with open(subtitles_file, 'r', encoding='utf-8') as file:
        file_content:str = file.read()
        
    # Remove italic, bold, font tags
    file_content = file_content.replace(r"<i>", "").replace(
            r"</i>", "").replace(r"<b>", "").replace(
            r"</b>", "").replace("<font>", "")

    # srt file file_contents new subtitle blocks after each consecutive pair of newline characters
    file_content = file_content.split("\n\n")
    
    print(file_content)
    return file_content


# Save subtitles into db for Searching purposes
def saveSubtitlesDb(video_id: int, file_content: str) -> bool:

    # FileNotFound
    if not video_id:
        raise VideoFileNotFoundException("Video File not founds")

    # Read each sentence
    for blocks in file_content:

        # 
        block:List[str] = blocks.strip().split("\n")
        
        if len(block) < 3 :
            continue
        
        number, time, *line = block
        # 00:00:00,500 --> 00:00:02,000
        # Convert time to HH:MM:SS,%f format
        
        # Skip font tag
        if number == 1:
            continue
        
        time = time.strip()[:12].replace(",",".")
        
        for sentence in line:
            for word in sentence.split(" "):
                word = removeOtherCharacters(word)
                if word:
                    # Save into DB
                    object = Subtitles(time=time, word=word, video=getVideoObject(video_id) )
                    object.save()
    return True
   
def getVideoObject(video_id:int)->Video:
    
    video = Video.objects.filter(video_id__iexact=video_id)
    if video:
        return video.first()
    
    return None

# Embed first subttitles track found into videos
def encodeVideoSubtitles(input_file: str, subtitles_fileName: str) -> str:

    print("Inside function")
    filename:str = input_file.split("/")[3]
    output_file:str = f"assets/output_videos/output_{filename}"
    command = f"ffmpeg -i {input_file[1:]} -vf subtitles={subtitles_fileName} {output_file}"

    try:
        output = subprocess.run(
            command, capture_output=True, shell=True, text=True)

    except Exception as e:
        print(e)
    print(output.stdout, output.stderr, "Message")
    return filename


def getVideoUrl(video_id:int)->str:

    data:str = Video.objects.filter(video_id__iexact=video_id)

    if not data:
        return ""

    return data.first().video_file.url
   
# Celery Task
@shared_task(bind=True)
def process_video(self, url:str, video_id:str)->None:
    
    cmd_output:str = checkSubtitlesStreams(url)
    streamCode:str = getAvailableSubtitles(cmd_output)
    subtitles_filename:str = convertToSrt(url, streamCode)
    encodeVideoSubtitles(url, subtitles_filename)
    print("encoding done")
    file_content:str = parse_srt(subtitles_filename)
    print("file reading done")
    saveSubtitlesDb(video_id ,file_content)
    print("subtitles saving done")
    
    print("Task Completed")
    
    return None