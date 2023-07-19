from django.contrib import admin
from django.urls import path
from blog.views import index, bloglist, blogdetails, blogwrite, create, edit, delete, search

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),
    path('bloglist/',bloglist),
    path('bloglist/<int:pk>',blogdetails, name='blogdetails'),
    path('blogwrite/',blogwrite),
    path('blog/create/',create, name="create"),
    path('bloglist/<int:pk>/edit/',edit, name="edit"),
    path('bloglist/<int:pk>/delete/',delete,name="delete"),
    path('bloglist/serach/', search, name="search")
]
