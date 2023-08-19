from django.contrib import admin
from django.forms import ModelForm

from .models import Post, Category, Tag
from persiantools.jdatetime import JalaliDateTime
from datetime import datetime
import pytz
from django.utils.html import format_html


class TagInline(admin.TabularInline):
    model = Post.tags.through
    verbose_name = 'تگ'
    verbose_name_plural = 'تگ ها'
    extra = 1


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_filter = ['status']
    inlines = [TagInline]
    list_editable = []

    def solar_date(self, obj):
        return obj.jalali_date_time

    def demo_url(self, obj):
        return format_html(f'<a href="{obj.get_absolute_url()}">نمایش</a>')

    def get_fields(self, request, obj=None):
        if request.user.is_editor:
            return ['title', 'short_description', 'content', 'image', 'category', 'post_id']
        elif request.user.is_journalist:
            return ['title', 'short_description', 'content', 'image', 'category', 'post_id', 'status']
        else:
            return ['title', 'short_description', 'content', 'image', 'category', 'post_id', 'status']

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
            return ['title', 'category', 'solar_date', 'status', 'demo_url']
        if request.user.is_journalist:
            return ['title', 'category', 'solar_date', 'author', 'status', 'demo_url']
        return ['title', 'category', 'solar_date', 'author', 'reviewer', 'status', 'demo_url']

    solar_date.short_description = 'تاریخ انتشار'
    demo_url.short_description = 'حالت دمو'


admin.site.register(Category)
admin.site.register(Tag)
