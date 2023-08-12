from django.contrib import admin

from .models import Journalist, Editor

admin.site.register(Journalist)
admin.site.register(Editor)
