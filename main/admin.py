from django.contrib import admin
from .models import Post
from tinymce.widgets import TinyMCE
from django.db import models

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    # fields = [
    #     'post_title',
    #     'post_summary',
    #     'post_content',
    #     'date_published'
    # ]
    #
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }

admin.site.register(Post, PostAdmin)
