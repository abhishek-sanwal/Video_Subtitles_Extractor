from django.db import models

# Create your models here.
import uuid

class Video(models.Model):
    
    video_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    video_file = models.FileField(upload_to="videos/")
    subtitles_data = models.TextField(blank=True)
    
    def __str__(self):
        
        return str(self.video_file)

    
    class Meta:
        
        db_table = "video_info"
        db_table_comment = " Django-Videos-Table-DND"
    
    
# Video--1 => N ----Subtitles Mapping 
class Subtitles(models.Model):
    
    video = models.ForeignKey(Video,on_delete=models.CASCADE)
    time = models.TimeField(auto_now=False,auto_now_add=False)
    word = models.CharField(max_length=800)
    
    class Meta:
        
        db_table = "video_subtitles"
        db_table_comment = " Django-Videos-Subtitles-Table-DND"
        ordering = ["time","word"]
    
    def __str__(self):
        
        return f"{self.video} {self.time} = {self.word}"