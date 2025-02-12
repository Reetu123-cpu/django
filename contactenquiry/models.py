from django.db import models

# Create your models here.
class contactenquiry(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=100)
    phoneno=models.CharField(max_length=100)
    message=models.CharField(max_length=100)


