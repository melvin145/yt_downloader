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
        video=YouTube(video_url)
        
        return FileResponse(open(video.streams.get_lowest_resolution().download(skip_existing=True),'rb'))
    else:
        return redirect('home')   
    return redirect('home')   
    


