from django.urls import path,include
from . import views

urlpatterns = [
    path('posts/',views.post_list,name='posts'),
    
]