from django.shortcuts import render,redirect
#from pytube import YouTube
from django.http import FileResponse
from pytube import YouTube
import pafy
def home(request):
    return render(request,"home.html")

def downloader(request):
    #SAVE_PATH="E:/"
    if request.method=='POST':
        video_url=request.POST['url']
        video=YouTube(video_url).streams.get_highest_resolution().download(skip_existing=True)
        
        return FileResponse(open(video,'rb'),as_attachment=True)
    else:
        return redirect('home')   
    return redirect('home')   
    
def audio(request):
    if request.method=='POST':
        url=request.POST['url']
        audio_url=YouTube(url)
        audio_to_download=audio_url.streams.filter(only_audio=True).all()
        audio=audio_to_download[1].download()

       
        return FileResponse(open(audio,'rb'),as_attachment=True,)
        


    return render(request,'audio_downloader.html')


