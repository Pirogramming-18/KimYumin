from django.db import models

class Idea(models.Model):
    name = models.CharField(max_length=32)
    image = models.FileField()
    description = models.TextField()
    interest = models.IntegerField()
    tool = models.TextChoices()

class Tool(models.Model):
    name = models.CharField(max_length=32)
    Kind = models.CharField(max_length=32)
    description = models.TextField()
    



# Create your models here.
