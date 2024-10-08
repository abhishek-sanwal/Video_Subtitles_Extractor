
import os
import logging

from celery import Celery
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE","video_subtitles_convertor.settings")

# Start celery app

app = Celery("Subtitles")

app.conf.enable_utc = False

app.conf.update(timezone= "Asia/Kolkata")
logging.basicConfig(level=logging.DEBUG)
app.config_from_object(settings, namespace="CELERY")

app.autodiscover_tasks()

# Bind a debug function 
@app.task(bind=True)
def debug_task(self):
    
    print(f"Request:{self.request!r}")