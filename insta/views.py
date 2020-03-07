from django.shortcuts import render
from django.http  import HttpResponse
import datetime as dt
from .models import Image, Post


def index(request):
    date = dt.date.today()
    images= Image.objects.all()
    posts= Post.objects.all()
    return render(request, 'insta/index.html', {"date": date,"images": images, "posts":posts})

def about(request):
    return render(request, 'insta/about.html')
    