from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Network(models.Model):
    name=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
class Show(models.Model):
    title=models.CharField(max_length=255)
    release_date=models.DateField()
    network=models.ForeignKey(Network,related_name="shows",on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    desc=models.TextField()