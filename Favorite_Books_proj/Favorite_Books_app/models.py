from django.db import models
import re
# Create your models here.
class BooksManager(models.Manager):
    def validator(self,postData):
        errors={}
        if len(postData['title'])<1:
            errors['title']='Title is required'
        if len(postData['desc'])<5:
            errors['desc']='Description at least 5 characters'
        return errors

class UserManager(models.Manager):
    def validator(self,postData):
        errors={}
        NAME_REGEX = re.compile(r'^[a-zA-Z]+$')
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        if len(postData['first_name'])<2:
            errors['first_name']='First name should be at lesat 2 charictors'
        elif not NAME_REGEX.match(postData['first_name']):
            errors['first_name']='First name should only be letters'
        if len(postData['last_name'])<2:
            errors['last_name']='Last name should be at lesat 2 charictors'
        elif not NAME_REGEX.match(postData['last_name']):
            errors['last_name']='Last name should only be letters'
        if not EMAIL_REGEX.match(postData['email']):                
            errors['email'] = "Invalid email address!"
        if len(postData['password'])<8:
            errors['password']='Password should be at lesat 8 charictors'
        elif postData['password'] != postData['confirm_pw']:
                errors['password'] = 'Confirm PW does not match the password!'
        user=Users.objects.filter(email=postData['email'])
        if user:
            errors['email']='Email is already exist'
        return errors

class Users(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=255)
    objects = UserManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Books(models.Model):
    title=models.CharField(max_length=255)
    desc=models.TextField()
    uploaded_by=models.name = models.ForeignKey(Users, related_name='books_uploaded', on_delete=models.CASCADE)
    users_who_like=models.ManyToManyField(Users,related_name="liked_books")
    objects=BooksManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

