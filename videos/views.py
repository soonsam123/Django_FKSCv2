from django.shortcuts import render
from .models import Video

def index(request):
    todos_videos = Video.objects.all()
    return render(request, 'videos/index.html', {'todos_videos': todos_videos})
