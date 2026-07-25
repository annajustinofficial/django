from django.db import models

class Item(models.Model):
    item_name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)
    price = models.CharField(max_length=100)

    def __str__(self):
        return self.item_name