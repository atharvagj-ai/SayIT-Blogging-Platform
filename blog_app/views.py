from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Post

# Create your views here.


def home(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'blog_app/home.html', context)

class PostListView(ListView):
    model = Post

def about(request): 
    return render(request, 'blog_app/about.html', {'title': 'About'})
