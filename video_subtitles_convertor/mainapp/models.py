from django.db import models

# Create your models here.


class Video(models.Model):
    
    video_name = models.CharField(max_length=600,blank=False,null=False)
    video_file = models.FileField(upload_to="videos/")
    
    def __str__(self):
        
        return self.video_name
    
    class Meta:
        
        db_table = "video_info"
        db_table_comment = " Django Videos Table_DND"
    
    
    
# class Subtitles(models.Model):
    
#     # video = models.ForeignKey(Video,on_delete=models.CASCADE)
#     start_time = models.TimeField(auto_now=False,auto_now_add=False)
#     end_time = models.TimeField(auto_now=False,auto_now_add=False)
#     phrase = models.CharField(max_length=800)
    
#     class Meta:
        
#         db_table = "video_subtitles"
#         db_table_comment = " Django Videos Subtitles Table_DND"
#         ordering = ["start_time","end_time","phrase"]
    
#     def __str__(self):
        
#         return f"{self.video_name} {self.start_time}=>{self.end_time} = {self.phrase}"