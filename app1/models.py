from django.db import models
from django.template.defaultfilters import slugify
import datetime
# Create your models here.
from ckeditor.fields import RichTextField

class Album(models.Model):
    artist = models.CharField(max_length=250)

    def __str__(self):
        return self.artist

class Song(models.Model):
    name = models.CharField(max_length=200)

class post(models.Model):
    post_content = RichTextField(('text here...'))