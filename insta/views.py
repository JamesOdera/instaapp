from django.shortcuts import render
from django.http  import HttpResponse
import datetime as dt
from .models import Image


def index(request):
    date = dt.date.today()
    images= Image.objects.all()
    return render(request, 'insta/index.html', {"date": date,"images": images})

def about(request):
    return render(request, 'insta/about.html')