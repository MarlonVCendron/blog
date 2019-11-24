from django.db import models
from datetime import datetime

# Create your models here.
class Post(models.Model):
    post_title = models.CharField(max_length=255)
    post_summary = models.CharField(max_length=255)
    preview_image = models.ImageField(upload_to='uploads/%Y/%m/%d/', default='/static/images/default_image.png')
    post_content = models.TextField()
    date_published = models.DateTimeField('date published', default=datetime.now())

    def __str__(self):
        return self.post_title
