from django.db import models

# Create your models here.

class EVend(models.Model):
    name = models.CharField(max_length=100)
    rating = models.IntegerField()
    code = models.IntegerField()

    class Meta:
        db_table = 'evend_info'


class EProd(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    qty = models.IntegerField()
    price = models.FloatField()
    active = models.BooleanField(default=True)

    class Meta():
        db_table = 'eprod_info'

