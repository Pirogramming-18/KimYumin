from django.shortcuts import render,redirect
from server.app.models import Idea,Tool

# Create your views here.

def idea_list(request):
    ideas = Idea.objects.all()
    return render(request,"idea/idea_list.html",{"ideas":ideas})

def idea_create(request):
    if request.method == "POST":
        Idea.objects.create(
            name=request.POST['name'],
            image=request.POST['image'],
            description = request.POST['description'],
            interest = request.POST['interest'],
            tool = request.POST['tool']
        )
        return redirect("/")    
    return render(request, "idea/idea_create.html")

def idea_detail(request,pk):
    idea = Idea.objects.all().get(pk=pk)
    return render(request,"idea/idea.html",{"idea":idea})

def idea_update(request.pk):
    idea = Idea.objects.all().get(pk=pk)
    if request.method == "POST":
        idea.name = request.POST['name']
        idea.image = request.POST['image']
        idea.description = request.POST['description']
        idea.interest = request.POST['interest']
        idea.tool = request.POST['tool']
        return redirect(f"idea/{idea.pk}")
    return render(request,"idea/idea_update.html",{"idea" : idea})





