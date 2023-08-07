from django import forms

from .models import Post, RawPost, Category, Tag


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        labels = {

        }
        widgets = {

        }


class RawPostForm(forms.ModelForm):
    class Meta:
        model = RawPost
        fields = '__all__'
        labels = {

        }
        widgets = {

        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        labels = {

        }
        widgets = {

        }


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'
        labels = {

        }
        widgets = {

        }
