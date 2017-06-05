# -*- coding: utf-8 -*-
from __future__ import unicode_literals


# Create your views here.
from django.shortcuts import render

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
    template = "blog/view.html"
    return render(request, template, context)

