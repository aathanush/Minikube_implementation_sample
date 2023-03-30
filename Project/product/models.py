from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    price = models.DecimalField(max_digits=100000, decimal_places=2)
    quantity = models.IntegerField()
    image = models.ImageField(default='./shopping/no_image.jpg',upload_to='')

