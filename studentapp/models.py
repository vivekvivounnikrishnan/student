from django.db import models


# Create your models here.
class School(models.Model):
    name=models.CharField(max_length=50)
    Place=models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.name
 
 ###############################################################################################################################################
 
class Batch(models.Model):
    school=models.ForeignKey(School,on_delete=models.CASCADE,null=True,blank=True)
    batch=models.CharField(max_length=50)
    batch_id=models.IntegerField()   
    
    def __str__(self):
        return self.batch
 ###############################################################################################################################################
 
class Student(models.Model):
    batch=models.ForeignKey(Batch,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=50)
    student_id=models.IntegerField()   
    def __str__(self):
        return self.name
    
################################################################################################################################################