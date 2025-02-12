from django.db import models

# Create your models here.
class rec(models.Model):
    Recepy_name=models.CharField(max_length=50)
    Description=models.TextField()
    Image=models.ImageField(upload_to="recipename")