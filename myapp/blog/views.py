from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Content

def index(request):
    contents = Content.objects.all()

    context = {
        'contents' : contents
    }
    return render(request, 'blog/index.html',context)

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
    if auth.authenticate:
        return render(request, 'blog/write.html')
    else:
        return render(request, 'blog/bloglist.html')



def create(request):
    content = Content()
    content.title = request.GET['title']
    content.content = request.GET['content']
    content.save()
    return redirect('/bloglist/' + str(content.pk))


def edit(request,pk):
    content = Content.objects.get(pk=pk)
    if request.method == 'POST':
        content.title = request.POST['title']
        content.content = request.POST['content']

        content.save()
        return redirect('/bloglist/' + str(content.pk))
    else:
        content = Content.objects.get(pk=pk)
        return render(request, 'blog/edit.html', {'content':content})
    

def delete(request,pk):
    content = Content.objects.get(pk=pk)
    content.delete()
    return redirect('/')


def search(request):
    content_list = Content.objects.all().order_by('-id')
    search = request.GET.get('search',"")
    print(search)
    if search:
        content_list = content_list.filter(title__icontains=search)
        return render(request, 'blog/search.html', {'content_list':content_list,'search':search})
    else:
        return render(request, 'blog/search.html')
