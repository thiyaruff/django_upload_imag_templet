from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Product(models.Model):
    desc = models.CharField(max_length=50,null=True,blank=True)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    image = models.ImageField(null=True,blank=True,default='/placeholder.png')
    createdTime=models.DateTimeField(auto_now_add=True)
    fields =['desc','price']
def __str__(self):
    return self.desc

