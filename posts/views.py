from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import HttpRequest

from .models import Post, Category, Tag
from accounts.models import User


def is_admin(user: User):
    return user.is_staff


# Admin - Journalist
class PostsView(View):

    def get(self, request: HttpRequest):
        posts = Post.objects.filter(status='C')
        return render(request, 'posts/posts.html', {'posts': posts, 'demo': ''})


class PostView(View):

    def get(self, request: HttpRequest, post_id):
        post = get_object_or_404(Post, id=post_id, status='C')
        return render(request, 'posts/post.html', {'post': post})


class PostsDemoView(View):
    def get(self, request: HttpRequest):
        # if is_admin(request.user):
        posts = Post.objects.all()
        return render(request, 'posts/posts.html', {'posts': posts, 'demo': 'demo'})
        # return render(request, '404.html')


class PostDemoView(View):
    def get(self, request: HttpRequest, post_id):
        # if is_admin(request.user):
        post = get_object_or_404(Post, id=post_id)
        return render(request, 'posts/post.html', {'post': post})
        # return render(request, '404.html')

# #  Admin, Journalist, Editor
# class CategoryDetail(View):
#
#     def get(self, request: HttpRequest):
#         pass
#
#     def post(self, request: HttpRequest):
#         pass
#
#     def put(self, request: HttpRequest):
#         pass
#
#     def delete(self, request: HttpRequest):
#         pass


# Admin, Journalist, Editor
# class TagDetail(View):
#
#     def get(self, request: HttpRequest):
#         pass
#
#     def post(self, request: HttpRequest):
#         pass
#
#     def put(self, request: HttpRequest):
#         pass
#
#     def delete(self, request: HttpRequest):
#         pass


# for show to client
