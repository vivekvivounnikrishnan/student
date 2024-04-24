from django.db import models

# Create your models here.######################################################################################################################


class Category(models.Model):
    name=models.CharField(max_length=50)
    desciption=models.CharField(max_length=50,default=1)
    
#################################################################################################################################################    
class Login(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.IntegerField()
    
    def _str_(self):
        return self.name


###################################################################################################################################################

    
    
class Product(models.Model):
    
    Productname=models.CharField(max_length=50)
    p_id=models.IntegerField()
    desc = models.CharField(max_length=100,null=True,blank=True)
    imagename=models.CharField(max_length=100,default=1)
    image=models.ImageField(upload_to='Product',default=1)
    
    def _str_(self):
        return self.Productname

class Categorycloth(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category')
    def __str__(self):
        return self.name
    
class Productcloth(models.Model):
    category = models.ForeignKey(Categorycloth,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='product')
    description = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Sizecategory(models.Model):
    size=models.CharField(max_length=100)
    def __str__(self):
        return self.size


class ProductVariant(models.Model):
#    SIZE=(
#     ('S','S'),
#     ('L','L'),
#     ('XL','XL')
#    )
#    csize=models.CharField(max_length=100,choices=SIZE,null=True,blank=True) THIS  OPTION IS GIVEN BY THE DEVELOPER AND NOT BY THE ADMIN
   product = models.ForeignKey(Productcloth,on_delete=models.CASCADE,null=True,blank=True)
   csize = models.ForeignKey(Sizecategory,on_delete=models.CASCADE,null=True,blank=True)
   actualprice=models.IntegerField()
   discountedprice = models.IntegerField()
   
   