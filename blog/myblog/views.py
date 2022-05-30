from django.shortcuts import render
from django.views import View

from .models import Post
# Create your views here.


class MainView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        return render(request, 'myblog/home.html', context={'posts': posts})
