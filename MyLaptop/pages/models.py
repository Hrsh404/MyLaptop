from django.db import models

# Create your models here.

class Client(models.Model): 
    name= models.CharField(max_length=255)
    monthlySales=models.IntegerField()
    photo= models.ImageField(upload_to="photos/%Y/%m/%d")
    facebookLink=models.URLField(max_length=100)
    twitterLink=models.URLField(max_length=100)
    googleLink=models.URLField(max_length=100)
    createdData=models.DateTimeField(auto_now_add=True)

    def __str__(self): 
        return self.name
