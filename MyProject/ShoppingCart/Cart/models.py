from django.db import models

# Create your models here.
class Product(models.Model):
    # id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    sku = models.CharField(max_length=30, unique=True)
    price = models.FloatField()
    quantity_in_stock = models.IntegerField()

    def __str__(self):
        return self.name


