from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=32)
    content = models.TextField()
    like = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class Comment(models.Model):
    postid = models.ForeignKey(Post,on_delete=models.CASCADE)
    content = models.TextField
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
# Create your models here.
