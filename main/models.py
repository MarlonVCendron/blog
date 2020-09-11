from django.db import models
from datetime import datetime

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    summary = models.CharField(max_length=511)
    preview_image = models.ImageField(upload_to='uploads/%Y/%m/%d/', default='/static/images/default_image.png')
    content = models.TextField()
    date_published = models.DateTimeField('date published', default=datetime.now())

    def __str__(self):
        return self.title
