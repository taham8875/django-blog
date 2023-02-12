from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

posts = [
    {
        'author': 'Taha',
        'title': 'blog post 1',
        'content': 'hello world',
        'date': '2023'
    },
    {
        'author': 'Omar',
        'title': 'blog post 2',
        'content': 'hello world 2',
        'date': '2013'
    }
]


def home(request):
    return render(request, 'blog/home.jinja2', context={'posts': posts})


def about(request):
    return render(request, 'blog/about.jinja2')
