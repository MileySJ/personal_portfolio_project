from django.shortcuts import render

def bloggy(request):
    return render(request, 'blog/blog.html')