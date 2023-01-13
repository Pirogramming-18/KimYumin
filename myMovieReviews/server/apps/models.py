from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=64)
    genre = models.CharField(max_length=32)
    content = models.TextField()
    rate = models.IntegerField()
    # date
