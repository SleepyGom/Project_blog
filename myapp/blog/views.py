from django.shortcuts import render, redirect
from .models import Content
def index(request):
    return render(request, 'blog/index.html')

def bloglist(request):
    contents = Content.objects.all()

    context = {
        'contents' : contents
    }
    return render(request, 'blog/bloglist.html', context)

def blogdetails(request, pk):
    content = Content.objects.get(pk=pk)

    context = {
        'content' : content
    }
    return render(request, 'blog/blogdetail.html', context)

def blogwrite(request):
    return render(request, 'blog/write.html')

def create(request):
    content = Content()
    content.title = request.GET['title']
    content.content = request.GET['content']
    content.save()
    return redirect('/bloglist/' + str(content.pk))