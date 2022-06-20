from django.shortcuts import render
from .models import Blog

def bloggy(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/blog.html', {'blogs':blogs})