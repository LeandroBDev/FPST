from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(fec_publicacion__lte=timezone.now()).order_by('fec_publicacion')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_list2(request):
    posts = Post.objects.filter(fec_publicacion__lte=timezone.now()).order_by('fec_publicacion')
    return render(request, 'blog/post_list2.html', {'posts': posts})