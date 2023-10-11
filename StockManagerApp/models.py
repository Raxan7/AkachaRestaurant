from django.db import models

from hotelmanagement.models import CustomUser


class Stock(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    quantity = models.PositiveIntegerField()
    expiration_date = models.DateField()
    reorder_quantity = models.PositiveIntegerField(default=10)  # Set your desired reorder threshold here

    def is_low_inventory(self):
        return self.quantity < self.reorder_quantity

    def __str__(self):
        return self.name


class RequestStock(models.Model):
    objects = models.Manager()
    name = models.ForeignKey(to=Stock, on_delete=models.CASCADE)


class ChefStockResource(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    quantity = models.PositiveIntegerField()
    expiration_date = models.DateField()
    reorder_quantity = models.PositiveIntegerField(default=10)

    def __str__(self):
        return self.name


class StockPurchases(models.Model):
    objects = models.Manager()
    seller_name = models.CharField(max_length=255)
    goods_bought = models.TextField()
    # goods_bought = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    # recorder = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)
    date_delivered = models.DateField(auto_now=True)

    def __str__(self):
        return self.seller_name
