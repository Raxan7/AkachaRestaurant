from django.db import models


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
