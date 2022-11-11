from django.db import models

# Create your models here.


class Category(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='category_photo')
    description = models.CharField(max_length=500, null=True)

    def __str__(self) -> str:
        return self.name
