from django.db import models

# Create your models here.
class Item(models.Model):
    item_name = models.CharField(max_length=200)
    item_quantity = models.IntegerField(default=0)
    item_price = models.IntegerField(default=0)


class Service(models.Model):
    service_name = models.CharField(max_length=200)
    service_quantity = models.IntegerField(default=0)
    service_price = models.IntegerField(default=0)