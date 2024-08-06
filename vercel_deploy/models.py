from django.db import models
from django.utils import timezone
# Create your models here.
class Test(models.Model):
    name = models.CharField(max_length=20)
    cons = models.CharField(max_length=200,default="测试")
  
    
    


class Contact(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    email= models.EmailField()

    def _unicode__(self):
        return self.name
    
class Tag(models.Model):
    contact = models.ForeignKey(Contact,on_delete=models.CASCADE,)
    name = models.CharField(max_length=50)
    def __unicode__(self):
        return self.name

class TimeTest(models.Model):
    name = models.CharField(max_length=20)
    cons = models.CharField(max_length=200)
    updated_at = models.DateTimeField(auto_now=True) 
    
