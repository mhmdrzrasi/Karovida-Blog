from django.db import models

from accounts.models import User
from .constants import STATUS_CHOICE
from persiantools.jdatetime import JalaliDate
from datetime import datetime
from django.utils.text import slugify


class Post(models.Model):
    class Meta:
        verbose_name = 'پست'
        verbose_name_plural = 'پست ها'

    title = models.CharField(max_length=256, help_text='حداکثر 256 کاراکتر', verbose_name='عنوان')
    short_description = models.TextField(max_length=512, help_text='حداکثر 512 کاراکتر', verbose_name='توضیح کوتاه')
    content = models.TextField(help_text='محتوا اصلی پست که به صورت HTML وارد شود', verbose_name='محتوا پست')
    image = models.ImageField(upload_to='uploads/', null=True, blank=True, verbose_name='عکس')

    slug = models.SlugField(blank=True, unique=True)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    publish_date = models.DateTimeField(null=True, blank=True, verbose_name='تاریخ انتشار')

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_author', verbose_name='نویسنده')
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='post_reviewer',
                                 verbose_name='بررسی کننده')

    category = models.ForeignKey('Category', on_delete=models.CASCADE, unique=True, related_name='post',
                                 verbose_name='دسته بندی')
    tags = models.ManyToManyField('Tag', blank=True, unique=True, related_name='post', verbose_name='برچسب ها')

    post_id = models.CharField(max_length=128, unique=True, help_text='به عنوان id داخل فایل HTML استفاده می شود')

    status = models.CharField(max_length=1, choices=STATUS_CHOICE, default='W', verbose_name='وضعیت')

    @property
    def jalali_date_time(self):
        ad_date = self.publish_date
        if not ad_date:
            return None
        #     If you want to display the 'time' at the same time, you can use JalaliDateTime
        return JalaliDate.to_jalali(datetime(ad_date.year, ad_date.month, ad_date.day))

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Category(models.Model):
    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    name = models.CharField(max_length=256, verbose_name='اسم')
    description = models.CharField(max_length=1024, null=True, blank=True, help_text='حداکثر 1024 کاراکتر',
                                   verbose_name='توضیحات')

    def __str__(self):
        return self.name


class Tag(models.Model):
    class Meta:
        verbose_name = 'برچسب'
        verbose_name_plural = 'برچسب ها'

    name = models.CharField(max_length=256, verbose_name='اسم')
    description = models.CharField(max_length=1024, null=True, blank=True, help_text='حداکثر 1024 کاراکتر',
                                   verbose_name='توضیحات')

    def __str__(self):
        return self.name


class Image(models.Model):
    image = models.ImageField()
