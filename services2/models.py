from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    marks=models.IntegerField(null=True,blank=True)
    email=models.EmailField()
    address=models.TextField(null=True,blank=True)
