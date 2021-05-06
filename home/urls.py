from django.urls import path, include
from django.contrib import admin
from .views import home,downloader,audio
urlpatterns=[
    path("" ,home,name="home"),
    path("download",downloader,name="downloader"),
    path("audio",audio,name='audio_downloader')
    
]

