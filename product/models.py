from django.db import models


# different category eg=men,women,children etc
class Category(models.Model):
    name= models.TextField(max_length=100)
    def __str__(self):
        return self.name
class Type(models.Model):
    name = models.TextField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
   
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    type =  models.ForeignKey(Type,on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
  


     
    