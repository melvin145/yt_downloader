from django.shortcuts import render,redirect
#from pytube import YouTube
from django.http import FileResponse
from pytube import YouTube
def home(request):
    return render(request,"home.html")

def downloader(request):
    SAVE_PATH="E:/"
    if request.method=='POST':
        video_url=request.POST['url']
        video=YouTube(video_url).streams.first().download(skip_existing=True)
        
        return FileResponse(open(video,'rb'),as_attachment=True)
    else:
        return redirect('home')   
    return redirect('home')   
    


