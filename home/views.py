from django.shortcuts import render,redirect
#from pytube import YouTube
from pytube import YouTube

# Create your views here.
def home(request):
    return render(request,"home.html")

def downloader(request):
    SAVE_PATH="E:/"
    if request.method=='POST':
        url=request.POST['url']
        video=YouTube(url)
        tittle=YouTube(url).title
        video.streams.get_lowest_resolution().download(SAVE_PATH)
        return render(request,'succes.html',{'title':tittle}) 
    else:
        return redirect('home')   
    return redirect('home')   
    


