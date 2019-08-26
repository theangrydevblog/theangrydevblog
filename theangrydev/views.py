from django.shortcuts import render
from theangrydev.models import Post, Content, Tag
# Create your views here.
def index(request):
    posts = Post.objects.all().order_by("-published")
    return render(request, "index.html", {'posts': posts})

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    contents = Content.objects.filter(post=post).order_by("timestamp")
    tags = Tag.objects.filter(posts__pk=pk)
    return render(request, "post.html",
                    {'post':post,
                    'contents':contents,
                    'tags': tags})
