from django.shortcuts import render
from .models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json 

def post_list(request):
    post = Post.objects.get(id=1)
    return render(request,'posts.html',{'post': post})

@csrf_exempt
def like_ajax(request):
    req = json.loads(request.body)
    like = req['like']
    post = Post.objects.get(id=1)

    if  like == 0:
        post.like = 1
        like = 1
    else:
        post.like = 0
        like = 0
    
    post.save()

    return JsonResponse({"like" : like})
   






# Create your views here.
