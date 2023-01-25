from django.db import models

# Create your models here.

class User(models.Model):
    role=models.CharField(max_length=30)
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    contact=models.CharField(max_length=14)
    email=models.EmailField(unique=True,max_length=40)
    password=models.CharField(max_length=30)
    
    def __str__(self):
        return self.role

class productsubcategory(models.Model):
    productid=models.CharField(max_length=5,null=True)
    productname=models.CharField(max_length=20,null=True)
    productprice=models.CharField(max_length=10,null=True,blank=True)  
    productimage=models.FileField(upload_to='media/images',default='media/samsung_mobile.jpg',null=True,blank=True) 
    productmodel=models.CharField(max_length=10,null=True,blank=True)
    productram=models.CharField(max_length=10,null=True,blank=True)
    
    def __str__(self):
        return self.productname