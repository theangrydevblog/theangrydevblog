from django.shortcuts import render
from theangrydev.models import Post, Content, Tag, Comment, Message
from theangrydev.dao import sql_templates
from theangrydev.forms import ContactForm
# Create your views here.

def index(request):
    posts = Post.objects.filter(draft=False).order_by("-published")
    return render(request, "index.html", {'posts': posts})

def tag_index(request):
    tag_sql = sql_templates["tag_count.sql"]
    tags = [{'id':id, 'name':name, 'count':count} for id, name, count in tag_sql.run()]
    return render(request, "tag_index.html", {
        'tags':tags
    })



def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    contents = Content.objects.filter(post=post).order_by("rank")
    tags = Tag.objects.filter(posts__slug=slug)
    comments = Comment.objects.filter(post=post)
    return render(request, "post.html",
                    {'post':post,
                    'contents':contents,
                    'comments': comments,
                    'tags': tags})

def tag_detail(request, name):
    tag = Tag.objects.filter(name=name).first()
    posts = tag.posts.all()
    return render(request, "tag.html", {
        'tag': tag,
        'posts': posts
    })


def about_me(request):
    return render(request, "about_me.html")

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            print(first_name,last_name,email,message)
            message = Message.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                message=message
            )

            return render(request, 'contact_success.html', {"first_name": first_name})
    else:
        form = ContactForm()
    return render(request, "contact.html", {"form": form})
