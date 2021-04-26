from django.db import models
from datetime import datetime
# Create your models here.
class ShowManager(models.Manager):
    def basic_validation(self, postData, extraData = ''):
        errors = {}
        date =datetime.today().date() 
        if len(postData['title'])<2:
            errors['title'] = 'Title Show should be at least 2 characters'
        one_show = Show.objects.filter(title=postData['title'])
        # this is my way to fix that
        if one_show and one_show[0].title != extraData:
            errors['title'] = "this title already Exists"
        if len(postData['network'])< 3:
            errors['network'] = 'Network should be at least 3 characters'
        if len(postData['desc'])< 10 and len(postData['desc']) > 0:
            errors['desc'] = 'Description Show should be at least 10 characters'
        if postData['date'] > str(date):
            errors['date'] = 'the date must be in the past!'
        return errors
                
class Show(models.Model):
    title=models.CharField(max_length=255)
    release_date=models.DateField()
    network=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    desc=models.TextField(default='')
    objects=ShowManager()
    
    def __str__(self):
        return self.title


# class Network(models.Model):
#     name=models.CharField(max_length=255)
#     created_at=models.DateTimeField(auto_now_add=True)
#     updated_at=models.DateTimeField(auto_now=True)