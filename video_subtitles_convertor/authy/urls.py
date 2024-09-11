

from django.urls import path
from django.contrib.auth import views as django_auth_views

from .views import Signup,Home

app_name="authy"

urlpatterns = [
    path('login/',django_auth_views.LoginView.as_view(template_name="authy/login.html"),name="login"),
    path('logout/',django_auth_views.LogoutView.as_view(template_name="authy/logout.html"),name="Logout"),
    path('register/',Signup.as_view(),name="signup"),
    path("home/",Home.as_view(),name="home")
]