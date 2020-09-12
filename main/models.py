from django.db import models
from datetime import datetime

# Create your models here.
class Post(models.Model):
    title_EN = models.CharField(max_length=255, default="")
    title_DE = models.CharField(max_length=255, default="")
    title_PT = models.CharField(max_length=255, default="")

    summary_EN = models.CharField(max_length=511, default="")
    summary_DE = models.CharField(max_length=511, default="")
    summary_PT = models.CharField(max_length=511, default="")

    content_EN = models.TextField(default="")
    content_DE = models.TextField(default="")
    content_PT = models.TextField(default="")

    preview_image = models.ImageField(upload_to='uploads/%Y/%m/%d/', default='static/default_image.png')
    date_published = models.DateTimeField('date published', default=datetime.now())

    def __str__(self):
        return self.title_EN
