from django.shortcuts import render
from django.http  import HttpResponse
from django.views.generic import ListView, CreateView
import datetime as dt
from .models import Image, Post
from django.contrib.auth.mixins import LoginRequiredMixin 


def index(request):
    date = dt.date.today()
    images= Image.objects.all()
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'insta/index.html', {"date": date,"images": images},context)

def about(request):
    return render(request, 'insta/about.html')

class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    ordering = ['-pub_date']
    template_name = 'insta/index.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = [ 'title', 'content', 'cover']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

def search_results(request):

    if 'post' in request.GET and request.GET["post"]:
        search_term = request.GET.get("post")
        searched_posts = Post.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'insta/search.html',{"message":message,"posts": searched_posts})

    else:
        message = "You haven't searched for any term"
        return render(request, 'insta/search.html',{"message":message})