from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt

# Create your views here.
def index(request):
    if 'user' in request.session:
        return redirect("/success")
    return render(request,"index.html")

def register(request):
    errors = User.objects.validator(request.POST)
    if len(errors)>0:
        for key,val in errors.items():
            messages.error(request,val)
        return redirect("/")
    else:
        if request.method=="POST":
            password=request.POST['password']
            passHash=bcrypt.hashpw(password.encode(),bcrypt.gensalt()).decode()
            User.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'],email=request.POST['email'],
            password=passHash,birthday=request.POST['date'])
            messages.success(request,"User successfully created")
        return redirect("/success")
def login(request):
    if request.method=="POST":
        user=User.objects.filter(email=request.POST['email'])
        if user:
            logged_user = user[0]
            if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
                request.session['user'] = logged_user.id
                messages.success(request,"Successfully logged in")
                return redirect("/success")
            else:
                messages.error(request,"Email or password is not correct")
                return redirect("/")
        else:
            messages.error(request,"Email or password is not correct")
            return redirect("/")

def success(request):
    if 'user' in request.session:
        user=User.objects.get(id=request.session['user'])
        print(user)
        return render(request,"success.html",{'user':user})
    else: 
        return redirect("/")
def logout(request):
    request.session.flush()
    return redirect("/")