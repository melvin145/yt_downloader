from django.shortcuts import render,redirect
#from pytube import YouTube
from pytube import YouTube

# Create your views here.
def home(request):
    return render(request,"home.html")

def downloader(request):
    if request.method=='POST':
        url=request.POST['url']
        video=YouTube(url)
        tittle=YouTube(url).title
        video.streams.get_highest_resolution().download
        return render(request,'succes.html',{'title':tittle}) 
    else:
        return redirect('home')   
    return redirect('home')    
        


