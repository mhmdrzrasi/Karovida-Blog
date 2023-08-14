from django.contrib import admin
from django.forms import ModelForm

from .models import Post, Category, Tag
from persiantools.jdatetime import JalaliDateTime
from datetime import datetime
import pytz

# admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Tag)


class PostAdmin(admin.ModelAdmin):
    list_filter = ['status']
    list_editable = []

    def solar_date(self, obj):
        return obj.jalali_date_time

    def get_fields(self, request, obj=None):
        if request.user.is_editor:
            return ['title', 'short_description', 'content', 'image', 'category', 'tags', 'post_id']
        elif request.user.is_journalist:
            return ['title', 'short_description', 'content', 'image', 'category', 'tags', 'post_id', 'status']
        else:
            return ['title', 'short_description', 'content', 'image', 'category', 'tags', 'post_id', 'status']

    def save_model(self, request, obj, form, change):
        if request.user.is_editor:
            obj.author = request.user  # Set author to current user (editor)
            obj.status = 'W'
            obj.reviewer = None
        else:
            try:
                obj.author
            except:  # If the person creating the post is not an editor
                obj.author = request.user  # Set author to current user (journalist)
            obj.reviewer = request.user  # Set reviewer to current user (journalist)

            if obj.status == 'C':
                utc_timezone = pytz.timezone('UTC')  # Use the 'UTC' timezone
                obj.publish_date = utc_timezone.localize(datetime.now())

        if obj.status != 'C':
            obj.publish_date = None
        super().save_model(request, obj, form, change)

    def get_list_display(self, request):
        if request.user.is_editor:
            return ['title', 'category', 'solar_date', 'slug', 'status']
        if request.user.is_journalist:
            return ['title', 'category', 'solar_date', 'slug', 'author', 'status']
        return ['title', 'category', 'solar_date', 'slug', 'author', 'reviewer', 'status']

    solar_date.short_description = 'تاریخ انتشار (اولین ایجاد)'


admin.site.register(Post, PostAdmin)
