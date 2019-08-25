from django.shortcuts import render
from theangrydev.models import Post, Content
# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, "index.html", {'posts': posts})

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    contents = Content.objects.filter(post=post).order_by("timestamp")
    return render(request, "post.html", {'post':post, 'contents':contents})
