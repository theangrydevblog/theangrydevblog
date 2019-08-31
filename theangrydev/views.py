from django.shortcuts import render
from django.db import connection as dbconn
from theangrydev.models import Post, Content, Tag
from theangrydev.dao import queries
# Create your views here.
dbconn = dbconn.cursor()

def index(request):
    posts = Post.objects.all().order_by("-published")
    return render(request, "index.html", {'posts': posts})

def tag_index(request):
    dbconn.execute(queries["tag_count.sql"])
    tags = [{'id':id, 'name':name, 'count':count} for id, name, count in dbconn.fetchall()]
    return render(request, "tag_index.html", {
        'tags':tags
    })



def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    contents = Content.objects.filter(post=post).order_by("timestamp")
    tags = Tag.objects.filter(posts__pk=pk)
    return render(request, "post.html",
                    {'post':post,
                    'contents':contents,
                    'tags': tags})

def tag_detail(request, pk):
    tag = Tag.objects.filter(pk=pk).first()
    posts = tag.posts.all()
    return render(request, "tag.html", {
        'tag': tag,
        'posts': posts
    })


def about_me(request):
    return render(request, "about_me.html")
