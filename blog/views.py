# -*- coding: utf-8 -*-
from __future__ import unicode_literals


# Create your views here.
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from django.views import generic

from blog.models import Post, Comment


def home(request):
    template_name = 'blog/home.html'
    posts = Post.objects.all()

    for i in posts:
        i.content = i.content[0:100] + "...."

    context = {'object_list': posts}
    return render(request, template_name, context)


def view_post(request, id):
    posts = Post.objects.get(id=int(id))
    comments = Comment.objects.filter(post=posts)
    context = {'posts': posts, 'comments': comments}
    template = "blog/post.html"
    return render(request, template, context)

def add_post(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        img = request.FILES['img']
        is_published = request.POST['is_published']
        user = User.objects.get(username=request.user.username)
        new_post = Post(title=title, content=content, img=img, is_published=is_published, user=user)
        new_post.save()
        return redirect('post', new_post.id)

    else:
        template = 'blog/add_post.html'
        context ={}
        return render(request, template, context)

def edit_post(request, pk):
    post = Post.objects.get(id=int(pk))
    if request.user.username != post.user.username:
        raise PermissionDenied
    if request.method == "GET":
        template = 'blog/post_edit.html'
        context = {'post':post}
        return render (request, template, context)
    else:
        post.title = request.POST['title']
        post.content = request.POST['content']

        if 'img' in request.FILES:
            post.img = request.FILES["img"]
        if 'is_published' in request.POST:
            post.is_published = request.POST['is_published']
        post.save()
        return redirect('post', post.id)

def del_post(request, pk):
    post = Post.objects.get(id=int(pk))
    if request.user.username != post.user.username:
        raise PermissionDenied
    if post is not None:
        post.delete()
        return redirect('home')

def signup(request):
    template = 'registration/signup.html'
    context ={}
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        user = User.objects.filter(email=email)
        if len(user) != 0:
            context['errors'] = "Email is already taken"
            return render(request, template, context)

        user = User.objects.filter(username=username)
        if len(user) != 0:
            context['errors'] = "Username is already taken"
            return render(request, template, context)

        if password1 == password2:
            user = User(first_name=firstname, last_name=lastname, email=email, username=username)
            user.set_password(password1)
            user.save()
            return redirect('login')
    return render(request, template, context)



