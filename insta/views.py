from django.shortcuts import render
from django.http  import HttpResponse

def index(request):
    return render(request, 'insta/index.html')

def about(request):
    return render(request, 'insta/about.html')