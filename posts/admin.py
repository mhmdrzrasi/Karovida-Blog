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
    list_display = ['title', 'author', 'category', 'solar_date', 'status', 'slug']
    list_filter = ['status']
    list_editable = []

    def solar_date(self, obj):
        return obj.jalali_date_time

    def get_fields(self, request, obj=None):
        if request.user.is_editor:  # Assuming is_editor attribute on User model
            return ['title', 'content', 'short_description', 'image', 'category', 'tags', 'post_id']
        elif request.user.is_journalist:  # Assuming is_journalist attribute on User model
            return ['title', 'content', 'short_description', 'image', 'category', 'tags', 'status', 'post_id']
        else:
            return ['title', 'content', 'short_description', 'image', 'category', 'tags', 'status', 'post_id']

    def save_model(self, request, obj, form, change):
        if request.user.is_editor:
            obj.author = request.user  # Set author to current user (editor)
            obj.status = 'W'
        elif request.user.is_journalist:
            obj.acceptor = request.user  # Set acceptor to current user (journalist)
            # if not obj.author:
            #     obj.author = request.user
            if obj.status == 'C':
                utc_timezone = pytz.timezone('UTC')  # Use the 'UTC' timezone
                obj.publish_date = utc_timezone.localize(datetime.now())
        super().save_model(request, obj, form, change)

    # def get_list_display(self, request):
    #     if request.user.is_superuser:
    #         self.list_editable.append('status')
    #     list_display = super().get_list_display(request)
    #     return list_display

    solar_date.short_description = 'تاریخ انتشار'


admin.site.register(Post, PostAdmin)
