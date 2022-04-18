from django.urls import path, include
from . Controllers.HomeController import home

urlpatterns = [
    path('', home.home, name='homeIAM'),
    path('home', home.home, name='homeIAM'),
    path('about', home.about, name='aboutIAM'),
]