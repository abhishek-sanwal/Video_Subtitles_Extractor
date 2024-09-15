

from .models import Video
from django import forms

class UploadVideoForm(forms.ModelForm):
    
    class Meta:
        
        model  = Video
        fields = ["video_file"]
        

# class SearchSubtitlesForm(forms.Form):
    
#     search_word = forms.CharField(max_length=40,required=True,widget=forms.TextInput(attrs={
#         'class': "form-control text-center fw-bold",
#         'style': 'max-width: auto;',
#         'placeholder': 'Enter Your word'
#     }))
    
#     video_name = forms.ModelChoiceField(queryset=Video.objects.all(),required=True,empty_label="Select Video",
#                                         widget=forms.Select(attrs={
#                                             'class':"form-select text-center fw-bold",'style':'max-width:auto;'
#                                         }))