from django.db import models

# Create your models here.

class Vendor(models.Model):
    name = models.CharField(max_length=100)
    rating = models.IntegerField()
    code = models.IntegerField()
    active = models.BooleanField(default=True)

    class Meta:
        db_table= 'vend_info'

class Product(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    qty = models.IntegerField()
    price = models.FloatField()
    active = models.BooleanField(default=True)

    class Meta():
        db_table = 'prod_info'

