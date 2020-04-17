from django.shortcuts import render
from theangrydev.models import Post, Content, Tag, Comment
from theangrydev.dao import sql_templates
# Create your views here.

def index(request):
    posts = Post.objects.all().order_by("-published")
    return render(request, "index.html", {'posts': posts})

def tag_index(request):
    tag_sql = sql_templates["tag_count.sql"]
    tags = [{'id':id, 'name':name, 'count':count} for id, name, count in tag_sql.run()]
    return render(request, "tag_index.html", {
        'tags':tags
    })



def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    contents = Content.objects.filter(post=post).order_by("timestamp")
    tags = Tag.objects.filter(posts__pk=pk)
    comments = Comment.objects.filter(post=post)
    return render(request, "post.html",
                    {'post':post,
                    'contents':contents,
                    'comments': comments,
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
