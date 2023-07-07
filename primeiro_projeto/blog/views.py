from django.shortcuts import render
from .models import Post


# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {
        'posts': posts
    })

def user_list(request):
    return render(request, 'blog/user.html', {})