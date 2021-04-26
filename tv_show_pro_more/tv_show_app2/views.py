from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from datetime import datetime
# Create your views here.
def index(request):
    return redirect("/shows")

def shows(request):
    context={
        "all_shows":Show.objects.all(),
    }
    return render(request,"show.html",context)
def new(request):
    return render(request,"create.html")
def create(request):
    errors = Show.objects.basic_validation(request.POST)
   
    if len(errors)>0:
        for key,val in errors.items():
            messages.error(request,val,key)
        return redirect('/shows/new')
    else:
        if request.method=="POST":
            new_show=Show.objects.create(title=request.POST['title'],release_date=request.POST['date']
            ,network=request.POST['network'],desc=request.POST['desc'])
        return redirect(f"/shows/{new_show.id}")
def read(request,id):
    context={
        "show":Show.objects.get(id=id),
    }
    return render(request,"read.html",context)
def edit(request,id):
    context={
        "show":Show.objects.get(id=id),
    }
    return render(request,"update.html",context)
def update(request,id):
    show=Show.objects.get(id=id)
    errors = Show.objects.basic_validation(request.POST, extraData = show.title)
    if len(errors)>0:
        for key,val in errors.items():
            messages.error(request,val,key)
        return redirect(f"/shows/{id}/edit")
    else:
        if request.method=="POST":
            show.title=request.POST['title']
            show.release_date=request.POST['date']
            show.network=request.POST['network']
            show.desc=request.POST['desc']
            show.save()
    return redirect(f"/shows/{show.id}")
def delete(request,id):
    show = Show.objects.get(id=id)
    show.delete()
    return redirect("/shows")