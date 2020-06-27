from django.shortcuts import render, redirect
from theangrydev.models import User, Post, Content, Tag, Comment, Message
from theangrydev.dao import sql_templates
from theangrydev.forms import ContactForm
from theangrydev.lib.oauth import GitHub
from urllib.parse import urlencode
from django.contrib.auth import login, logout
from django.urls import reverse


import os
import json
import requests
import urllib.parse as urlparse

github_login = GitHub(
    os.getenv('OAUTH_CLIENT_ID'),
    os.getenv('OAUTH_CLIENT_SECRET')
)

github_signup = GitHub(
    os.getenv('OAUTH_SIGNUP_CLIENT_ID'),
    os.getenv('OAUTH_SIGNUP_CLIENT_SECRET')
)
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

def sign_in(request):
    message = request.GET.get('message')

    # oauth_signup_url = urlparse.urlunparse(url_parts)
    oauth_url = github_login.get_oauth_url()
    oauth_signup_url = github_signup.get_oauth_url()
    return render(request, "sign_in.html", {
        'oauth_url': oauth_url,
        'oauth_signup_url': oauth_signup_url,
        'message': message
    })

def oauth_login(request):
    # GitHub redirects user to this view
    # https://www.theangrydev.io/oauth?code=3461291a4c10ba99d0e3&state=helloworld
    code = request.GET.get("code")
    state = request.GET.get("state")

    email, avatar_url = github_login.get_user_data(code)

    user = User.objects.filter(email=email).first()
    if not user:
        return redirect("/sign_in?message=No account found")
    if user.avatar != avatar_url:
        user.avatar = avatar_url
        user.save()

    login(request, user, backend='theangrydev.lib.backends.AngryDevAuth')

    return redirect('/')

def oauth_signup(request):
     # GitHub redirects user to this view
    # https://www.theangrydev.io/oauth?code=3461291a4c10ba99d0e3&state=helloworld
    code = request.GET.get("code")
    state = request.GET.get("state")

    email, avatar_url = github_signup.get_user_data(code)

    user = User.objects.filter(email=email).first()
    if not user:
        user = User.objects.create(
            email=email,
            avatar=avatar_url
        )

    oauth_url = github_login.get_oauth_url()
    return redirect(oauth_url)


def sign_out(request):
    logout(request)

    return redirect('/')

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
