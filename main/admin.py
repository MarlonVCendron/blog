from django.contrib import admin
from .models import Post
# from tinymce.widgets import TinyMCE
from django.db import models

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Title', {'fields': ['title_EN', 'title_DE', 'title_PT']}),
        ('Summary', {'fields': ['summary_EN', 'summary_DE', 'summary_PT']}),
        ('Content', {'fields': ['content_EN', 'content_DE', 'content_PT']}),
        ('Image / Date', {'fields': ['preview_image', 'date_published']}),
    ]

admin.site.register(Post, PostAdmin)
# admin.site.register(Post)
