from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
import bcrypt
# Create your views here.
def index(request):
    if 'user' in request.session:
        return redirect("/books")
    else:
        return render(request,"reg_login.html")
def register(request):
    errors = Users.objects.validator(request.POST)
    if len(errors)>0:
        for key,val in errors.items():
            messages.error(request,val)
        return redirect("/")
    else:
        if request.method=="POST":
            password=request.POST['password']
            passHash=bcrypt.hashpw(password.encode(),bcrypt.gensalt()).decode()
            Users.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'],email=request.POST['email'],
            password=passHash)
            messages.success(request,"User successfully created")
        return redirect("/books")
def login(request):
    if request.method=="POST":
        user=Users.objects.filter(email=request.POST['email'])
        if user:
            logged_user = user[0]
            if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
                request.session['user'] = logged_user.id
                messages.success(request,"Successfully logged in")
                return redirect("/books")
            else:
                messages.error(request,"Email or password is not correct")
                return redirect("/")
        else:
            messages.error(request,"Email or password is not correct")
            return redirect("/")

def books(request):
    if 'user' in request.session:
        context={
            "user":Users.objects.get(id=request.session['user']),
            "all_books":Books.objects.all()
        }
        return render(request,"books.html",context)
    else: 
        return redirect("/")
def logout(request):
    request.session.flush()
    return redirect("/")

def add_book(request):
    errors = Books.objects.validator(request.POST)
    if len(errors)>0:
        for key,val in errors.items():
            messages.error(request,val)
        return redirect("/books")
    else:
        if request.method=="POST":
            user=Users.objects.get(id=request.session['user'])
            book=Books.objects.create(title=request.POST["title"],
            desc=request.POST["desc"],uploaded_by=user)
            book.users_who_like.add(user)
        return redirect("/books")

def add_to_fav(request,id):
    book=Books.objects.get(id=id)
    user=Users.objects.get(id=request.session['user'])
    book.users_who_like.add(user)
    return redirect(f"/books/{book.id}")

def get_book(request , id):
    context={
    'book':Books.objects.get(id=id),
    'user':Users.objects.get(id=request.session['user'])
    }
    return render(request,"get_book.html",context)

def update_book(request,id):
    book=Books.objects.get(id=id)
    book.title=request.POST['title']
    book.desc=request.POST['desc']
    book.save()
    return redirect(f"/books/{book.id}")

def delete_book(request,id):
    book=Books.objects.get(id=id)
    book.delete()
    return redirect("/books")

def unfav_book(request,id):
    book=Books.objects.get(id=id)
    user=Users.objects.get(id=request.session['user'])
    book.users_who_like.remove(user)
    return redirect(f"/books/{book.id}")

def mylist(request):
    context={
        'user':Users.objects.get(id=request.session['user'])
    }
    return render(request,"my_book.html",context)