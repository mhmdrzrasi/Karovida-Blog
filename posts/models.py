from django.db import models

from accounts.models import User
from .constants import STATUS_CHOICE


class Post(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    image = models.ImageField()
    slug = models.SlugField()
    publish_date = models.DateField()

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='post')
    tags = models.ManyToManyField('Tag', related_name='post')

    status = models.CharField(max_length=1, choices=STATUS_CHOICE)

    def __str__(self):
        return self.title


class RawPost(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    image = models.ImageField()
    slug = models.SlugField()
    publish_date = models.DateField()

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='raw_post')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='raw_post')
    tags = models.ManyToManyField('Tag', related_name='raw_post')

    status = models.CharField(max_length=1, choices=STATUS_CHOICE)


    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=1024)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=1024)

    def __str__(self):
        return self.name


class Image(models.Model):
    image = models.ImageField()
