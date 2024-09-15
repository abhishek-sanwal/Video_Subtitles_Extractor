
from django import template
from ..models import Video

register= template.Library()


@register.filter
def get_output_url(instance):
    
    if isinstance(instance,Video):
        
        return instance.video_file.url.replace("videos","output-videos")
    
    return ""

