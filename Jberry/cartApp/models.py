from django.db import models
# from django.contrib.admin.models import User
from authentication.models import User
from product.models import Product
# Create your models here.


class Cart(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    uid = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    pid = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    qnt = models.BigIntegerField(default=0)
    price = models.FloatField(max_length=100, default=0.00)
    order = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'Cart(id={self.id} uid={self.uid} pid={self.pid})'
