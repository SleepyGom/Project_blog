from django.urls import path
from . import views

urlpatterns = [
    path('',views.postlist, name='postlist'),
    path('<int:pk>/',views.postdetail, name='postdetail'),
    path('write/',views.write, name='postwrite'),
    path('edit/<int:pk>',views.edit, name='postedit'),
    path('delete/<int:pk>',views.delete, name='postdelete'),

    
]