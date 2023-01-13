from django.db import models

# Create your models here.

class Review(models.Model):
    title = models.CharField(max_length=64)
    genre = models.CharField(max_length=32)
    content = models.TextField()
    date = models.IntegerField()
    director = models.CharField(max_length=32)
    actor = models.CharField(max_length=32)
    runningtime = models.IntegerField()
    rate = models.FloatField()
    # date
