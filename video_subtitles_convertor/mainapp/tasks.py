
from celery import shared_task
from .models import Video, Subtitles
from .CustomException import NoSubtitlesException, VideoFileNotFoundException
from typing import List
import subprocess

# A  lambda function to remove special characters and numbers 
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
    return cmd_output.stderr

# Check all available subtitles streams and choose the first
def getAvailableSubtitles(cmd_output: str) -> str:

    # Get each line of output
    streamCode: str = ""

    # Process line-by-line
    for line in cmd_output.split("\n"):
        
        # Fetch each word from line
        word: List[str] = line.strip().split()

        # We are using first subtitles track to put it on video
        # fetch first subtitles track from file
        if word and word[0] == "Stream" and (word.count("Subtitle:") > 0 or word.count("subtitle") > 0):

            print("streamCode", word[1][1:4])
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

    lis = list()
    # Read each sentence
    for blocks in file_content:

        # 
        block:List[str] = blocks.strip().split("\n")
        
        if len(block) < 3 :
            continue
        
        number, time, *line = block
        # 00:00:00,500 --> 00:00:02,000
        # Convert time to HH:MM:SS,%f format
        lis.append(" ".join(line))
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
    print(lis)
    video = getVideoObject(video_id)
    print(video,"Video Name")
    video.subtitles_data = "\n".join(lis)
    video.save()
    
    return True
   
def getVideoObject(video_id)->Video:
    
    
    video_id = str(video_id)
    video = Video.objects.filter(video_id__iexact=video_id)
    if video:
        return video.first()
    print(video_id, video)
    return None

# Embed first subtitles track found into videos
def encodeVideoSubtitles(input_file: str, subtitles_fileName: str) -> str:

    print("Inside function")
    filename:str = input_file.split("/")[3]
    output_file:str = f"assets/output_videos/output-{filename}"
    command = f"ffmpeg -i {input_file[1:]} -vf subtitles={subtitles_fileName} {output_file}"

    output = subprocess.run(
        command, capture_output=True, shell=True, text=True)
    
    return filename

# Celery Task
@shared_task(bind=True)
def process_video(self, url:str, video_id:str)->None:
    
    cmd_output:str = checkSubtitlesStreams(url)
    streamCode:str = getAvailableSubtitles(cmd_output)
    subtitles_filename:str = convertToSrt(url, streamCode)
    file_content:str = parse_srt(subtitles_filename)
    print("file reading done")
    saveSubtitlesDb(video_id ,file_content)
    print("subtitles saving done")
    encodeVideoSubtitles(url, subtitles_filename)
    print("encoding done")
    
    print("Task Completed")
    
    return None