from django.shortcuts import render
from django.views import View
from django.http import HttpRequest

from .models import Post, RawPost, Category, Tag
from .forms import PostForm, RawPostForm, CategoryForm, TagForm


# Admin, Journalist, Editor
class RawPostDetail(View):

    def get(self, request: HttpRequest):
        pass

    def post(self, request: HttpRequest):
        pass

    def put(self, request: HttpRequest):
        pass

    # except Editor
    def delete(self, request: HttpRequest):
        pass


# Admin - Journalist
class PostDetail(View):

    def get(self, request: HttpRequest):
        pass

    def post(self, request: HttpRequest):
        pass

    def put(self, request: HttpRequest):
        pass

    def delete(self, request: HttpRequest):
        pass


#  Admin, Journalist, Editor
class CategoryDetail(View):

    def get(self, request: HttpRequest):
        pass

    def post(self, request: HttpRequest):
        pass

    def put(self, request: HttpRequest):
        pass

    def delete(self, request: HttpRequest):
        pass


# Admin, Journalist, Editor
class TagDetail(View):

    def get(self, request: HttpRequest):
        pass

    def post(self, request: HttpRequest):
        pass

    def put(self, request: HttpRequest):
        pass

    def delete(self, request: HttpRequest):
        pass


# for show to client
class PostView(View):

    def get(self, request: HttpRequest):
        pass
