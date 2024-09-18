
from django import template
from ..models import Video
from typing import Union
register= template.Library()


@register.filter
def get_output_url(instance)->Union[str,None]:
    
    if isinstance(instance,Video):
        
        return instance.video_file.url.replace("videos","output-videos")
    
    return ""


@register.filter
def getFileName(url:str)->str:
    
    arr = url.split("/")
    return arr[3]
    

