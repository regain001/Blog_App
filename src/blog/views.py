from django.shortcuts import render
from django.http import HttpResponse

from .models import Post
posts = [
    {
        'author': 'Mukbul',
        'title': 'Blog Post 1',
        'content': 'first post content',
        'date_posted': 'Feb 7, 2019'
    },
    {
        'author': 'Reason',
        'title': 'Blog Post 2',
        'content': 'second post content',
        'date_posted': 'Feb 7, 2019'
    }
]

# Home page of Blog Website...
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request,'blog/home.html',context)


def about(request):
    return render(request,'blog/about.html',{'title':'about'})
