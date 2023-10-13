from django.db import models

# Create your models here.
class Doctordeatails(models.Model):
    doctorname=models.CharField(max_length=100)
    image=models.ImageField(upload_to="doctordeatails_images")
    description=models.CharField(max_length=100)
    fees=models.IntegerField()
    
    
