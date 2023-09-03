from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class AppliedUserData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    Firstname=models.CharField(max_length=100)
    Lastname=models.CharField(max_length=100)
    job_role=models.CharField(max_length=100)
    phonenumber=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    my_image = models.ImageField(null=True,blank=True)
