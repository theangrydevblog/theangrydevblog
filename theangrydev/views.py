from django.shortcuts import render, redirect
from theangrydev.models import User, Post, Content, Tag, Comment, Message
from theangrydev.dao import sql_templates
from theangrydev.forms import ContactForm
from urllib.parse import urlencode
from django.contrib.auth import login

import os
import json
import requests
import urllib.parse as urlparse
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
    base = "https://github.com/login/oauth/authorize"
    client_id = os.getenv("OAUTH_CLIENT_ID")
    state = "helloworld"

    params = {
        "client_id": client_id,
        "state": state,
    }

    url_parts = list(urlparse.urlparse(base))
    url_parts[4] = urlencode(params)

    oauth_url = urlparse.urlunparse(url_parts)

    return render(request, "sign_in.html", {
        'oauth_url': oauth_url
    })

def oauth(request):
    # GitHub redirects user to this view
    # https://www.theangrydev.io/oauth?code=3461291a4c10ba99d0e3&state=helloworld
    code = request.GET.get("code")
    state = request.GET.get("state")

    client_id = os.getenv("OAUTH_CLIENT_ID")
    client_secret = os.getenv("OAUTH_CLIENT_SECRET")

    # Get access token
    resp = requests.get("https://github.com/login/oauth/access_token", params={
        "client_id": client_id,
        "client_secret": client_secret,
        "code": code,
        "redirect_uri": "",
        "state": state
    }, headers={
        "Accept": "application/json"
    })

    access_token = json.loads(resp.content)["access_token"]

    # Get Github user data
    resp = requests.get("https://api.github.com/user", headers={
        "Authorization": f"token {access_token}"
    })

    github_user = json.loads(resp.content)

    avatar_url = github_user['avatar_url']
    email = github_user['email']

    user = User.objects.filter(email=email).first()
    if user.avatar != avatar_url:
        user.avatar = avatar_url
        user.save()

    login(request, user)

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
