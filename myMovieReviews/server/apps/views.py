from django.shortcuts import render,redirect
from .models import Review


def review_list(request,*args,**kwargs):
    reviews = Review.objects.all()
    return render(request,"review_list.html",{"reviews" : reviews})

def review_details(request,pk,*args,**kwargs):
    review = Review.objects.all().get(id=pk)
    return render(request,"review_details.html",{"review" : review})

def review_create(request,*args,**kwargs):
    if request.method == "POST":
        Review.objects.create(
            title=request.POST['title'],
            genre=request.POST['genre'],
            director=request.POST['director'],
            actor = request.POST['actor'],
            rate = request.POST['rate'],
            runningtime = request.POST['runningtime'],
            content = request.POST['content'], 
        )
        return redirect("/")
    return render(request,"review_create.html")

def review_update(request,pk,*args,**kwargs):
        review = Review.objects.get(id=pk)
        if request.method == "POST":
            
            review.title = request.POST['title']
            review.director = request.POST['director']
            review.actor = request.POST['actor']
            review.rate = request.POST['rate']
            review.genre = request.POST['genre']
            review.runningtime = request.POST['runningtime']
            review.content = request.POST['content']
            review.save()
            return render(request, "review_details.html",{"review" : review})
        
            # return redirect(f"review/{review.id}")
        return render(request, "review_update.html", {"review" : review})
    
def review_delete(request,pk,*args,**kwargs):
    if request.method == "POST":
        review = Review.objects.get(id=pk)
        review.delete()
    return redirect("/")

# Create your views here.
