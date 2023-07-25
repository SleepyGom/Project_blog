from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DeleteView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post, Category, Tag, Comment
from .forms import CommentForm
from django.utils.text import slugify
from django.db.models import Q

class PostList(ListView):
    model = Post
    ordering = '-pk'

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all().order_by('-name')
        context['no_category_post_count'] = Post.objects.filter(category = None).count()
        return context
    
    def get_queryset(self):
        queryset = super().get_queryset()
        search_keyword = self.request.GET.get('q')

        if search_keyword:
            queryset= queryset.filter(
                Q(title__icontains=search_keyword) |
                Q(content__icontains=search_keyword) |
                Q(tags__name__icontains=search_keyword)).distinct()
        return queryset
    

class PostDetail(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetail,self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all().order_by('-name')
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        context['comment_form'] = CommentForm
        return context
    
    
def category_page(request, slug):
    category = Category.objects.get(slug=slug)
    categories = Category.objects.all().order_by('-name')
    context = {
        'post_list' : Post.objects.filter(category=category).order_by('-pk'),
        'categories' : categories,
        'no_category_post_count' : Post.objects.filter(category=None).count(),
        'category':category,
        'category_list' : Category.objects.all().order_by('-name')
    }

    return render(request, 'blog/post_list.html', context)


def tag_page(request,slug):
    tag = Tag.objects.get(slug=slug)
    post_list = tag.post_set.all()
    categories = Category.objects.all().order_by('-name')
    context = {
        'post_list' : post_list,
        'categories' : categories,
        'no_category_post_count' : Post.objects.filter(category=None).count(),
        'tag' : tag,
        'category_list': Category.objects.all().order_by('-name')
        }
    
    return render(request,'blog/post_list.html',context)


class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'file_upload', 'category', 'tags']

    def form_valid(self,form):
        current_user = self.request.user
        if current_user.is_authenticated:
            form.instance.author = current_user
            
            response = super(PostCreate,self).form_valid(form)

            tags_str = self.request.POST.get('tags_str')

            if tags_str:
                tags_str = tags_str.strip()
                tags_str = tags_str.replace(',',';')
                tags_list = tags_str.split(';')
                for t in tags_list:
                    t = t.strip()
                    tag, is_tag_created = Tag.objects.get_or_create(name=t)
                    if is_tag_created:
                        tag.slug = slugify(t,allow_unicode=True)
                        tag.save()

                    self.object.tags.add(tag)
            return response
        else:
            return redirect('/blog/')
        

class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'content','file_upload', 'category', ' tags']

    def form_valid(self,form):
        current_user = self.request.user
        if current_user.is_authenticated:
            form.instance.author = current_user
            return super(PostUpdate,self).form_valid(form)
        else:
            return redirect('/blog/')
        
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            post = self.get_object()
            if post.author == request.user:
                return super().dispatch(request,*args,**kwargs)
            else:
                return HttpResponse('로그인 이후 사용하실 수 있습니다.')
        return super().dispatch(request, *args,**kwargs)
    
postlist = PostList.as_view()
postdetail = PostDetail.as_view()
write = PostCreate.as_view()
edit = PostUpdate.as_view()
delete = DeleteView.as_view()