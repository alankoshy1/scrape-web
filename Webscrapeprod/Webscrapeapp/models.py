from django.db import models

# Create your models here.
class Scrap(models.Model):

    def __str__(self):
         return  self.sitename
    address=models.CharField(max_length=500,null=True,blank=True)
    sitename=models.CharField(max_length=250,null=False,blank=True)

