from typing import Any, Dict
from django.db.models.query import QuerySet
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
        context['category_list'] = Category.objects.filter(category = None).count()
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
    

postlist = PostList.as_view()