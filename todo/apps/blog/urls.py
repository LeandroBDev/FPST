from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    #url('', views.post_list, name='post_list'),
    #url('ls', views.post_list2, name='post_list2'),
    path('', views.post_list),
    path('articles/', views.post_list2),
]