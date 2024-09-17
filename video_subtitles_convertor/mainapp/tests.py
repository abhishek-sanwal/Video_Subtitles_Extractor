
from django.test import TestCase, Client
from django.core.files import File
from django.db.models import Q
from django.urls import reverse
import uuid
import mock
import os
from .models import Video, Subtitles

class ModelTest(TestCase):
    
    def setUp(self) -> None:
        
        self.video_id = uuid.uuid4()
        self.video_file = mock.MagicMock(spec=File)
        self.video_file.name = 'test_video.mp4'
        self.video = Video(video_id=self.video_id, 
                           video_file=self.video_file)
        
        self.video.save()
        
        self.time = "00:00:34"
        self.word = "random"
        self.subtitle = Subtitles(video=self.video, 
                                  time=self.time, 
                                  word=self.word)
        self.subtitle.save()

    
    def test_readModel(self):
        # For Video Model
        video_object = Video.objects.get(video_id=self.video_id)
        self.assertIsNotNone(video_object, 
                             "Video Object is Not equal to None")
        self.assertIsInstance(video_object, Video, 
                              "Video_Object is object of Video Model")
        self.assertEqual(video_object, self.video, 
                         "Video Object is same as video")
        
        # For Subtitle Model
        subtitle = Subtitles.objects.filter(video=self.video, 
                                            time=self.time, 
                                            word=self.word).first()
        self.assertIsNotNone(subtitle, 
                             "Subtitle object is not found")
        self.assertIsInstance(subtitle, Subtitles, 
                              "Subtitle object is object of subtitles")
        self.assertEqual(subtitle, self.subtitle, 
                         "Subtitles object is same as subtitle")    
    
    def test_attributeValidation(self):
        
        # For Video Model
        self.assertTrue(self.video.video_id == self.video_id,
                        "Video_Id is same.")
        
        # For Subtitles Model
        self.assertTrue(self.subtitle.video == self.video,
                        "Foreign key working")
        self.assertTrue(self.subtitle.time == self.time,
                        "Time of subtitle object is correct")
        self.assertTrue(self.subtitle.word == self.word,
                        "Word of subtitle object is correct")
        
    def test_updateModel(self):
        
        # Update data for Subtitles Model
        self.subtitle.word = "Gautam"
        self.subtitle.time = "00:00:27"
        self.subtitle.save()
        
        # Assertion for Subtitles model
        self.assertNotEqual(self.subtitle.word,self.word,
                            " Subtitle word update")
        self.assertNotEqual(self.subtitle.time,self.time,
                            " Subtitle word update")
        
        # Restore state for Subtitles Model
        self.subtitle.word = self.word
        self.subtitle.time = self.time
        self.subtitle.save()
     
    def test_deleteModel(self):
        # Delete Video Model
        self.video.delete()
        self.assertFalse(Video.objects.filter(video_id=self.video.video_id).exists(),
                         "Video deletion")
        
        # Delete Subtitles Model
        self.subtitle.delete()
        self.assertFalse(Subtitles.objects.filter(video_id=self.subtitle.id).exists(),
                         "Subtitle deletion")
        
        
        
class ViewTest(TestCase):
    
    def setUp(self) -> None:

        self.client = Client()
    
        self.upload_video_url = reverse('mainapp:upload-video'),
        self.list_videos_url = reverse('mainapp:list-videos'),
        self.search_subtitles_url = reverse('mainapp:search-subtitles')
        # print(type(self.upload_video_url),self.list_videos_url)
        
    def test_UploadVideoView_GET(self):
        
        response = self.client.get(self.upload_video_url[0])
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "mainapp/upload-video.html")
        self.assertTemplateUsed(response, "mainapp/base.html")
        
        
    def test_ListVideoView_GET(self):
        
        response = self.client.get(self.list_videos_url[0])
        
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "mainapp/list-video.html")
        self.assertTemplateUsed(response, "mainapp/base.html")
        
        
    def test_SubtitleDetailsView_GET(self):
        
        response = self.client.get(self.search_subtitles_url)
        
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "mainapp/list-subtitles.html")
        self.assertTemplateUsed(response, "mainapp/base.html")
        
        
    
        
            
    
    
    
        
            