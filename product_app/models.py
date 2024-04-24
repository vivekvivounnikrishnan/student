from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=50)
    img=models.ImageField(upload_to='Product')
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=50)
    img=models.ImageField(upload_to='Product')
    descript=models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Size(models.Model):
    Product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=50)
    img=models.ImageField(upload_to='Product')
    descript=models.CharField(max_length=50)
    
    def __str__(self):
        return self.name