from django.shortcuts import render,redirect
from server.apps.models import Movie


def movie_list(request):
    posts = Movie.objects.all()
    return render(request,"movie_list.html",{"posts":posts})
# Create your views here.
