from email.policy import default
from unicodedata import name
from django.db import models

from category.models import Category

# Create your models here.


class Product(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=50)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, blank=True, null=True
    )
    description = models.TextField(max_length=500, null=True)
    price = models.FloatField()
    weight = models.FloatField()
    deliver = models.SmallIntegerField(default=7)
    in_stock = models.BooleanField(default=True)
    image = models.ImageField(upload_to='product_photo')

    def __str__(self) -> str:
        return self.name
