from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import CreateView, View
from django.http import HttpResponse

from .forms import SignupForm


class Signup(CreateView):
    
    form_class = SignupForm
    template_name = "authy/signup.html"
    success_url=reverse_lazy("authy:login")
    
class Home(View):
    
    def get(self, request):
        
        return HttpResponse(f"<h2> Welcome {request.user} to our app</h2>")
    
    