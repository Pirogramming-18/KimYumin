from django.db import models


class Register(models.Model):
    title = models.CharField(max_length=32)
    image = models.ImageField()
    description = models.TextField()
    interest = models.IntegerField()
    tool = models.Choices()

# Create your models here.
