from django.contrib import admin
from django.urls import path
from blog.views import index, bloglist, blogdetails, blogwrite, create, edit, delete, search
from account.views import login, signin,logout

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',index, name='index'),
    path('bloglist/',bloglist),
    path('bloglist/<int:pk>',blogdetails, name='blogdetails'),
    path('blogwrite/',blogwrite, name="write"),
    path('blog/create/',create, name="create"),
    path('bloglist/<int:pk>/edit/',edit, name="edit"),
    path('bloglist/<int:pk>/delete/',delete,name="delete"),
    path('bloglist/serach/', search, name="search"),
    path('login/', login, name="login"),
    path('signin/', signin, name="signin"),
    path('logout/',logout, name="logout")
]
