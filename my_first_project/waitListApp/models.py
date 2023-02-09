from django.db import models


class Investment(models.Model):
    stock = models.CharField(max_length=50)
    category = models.CharField(max_length=20)
    share_price = models.DecimalField(max_digits=10, decimal_places=2)
    investment = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    date = models.DateField()
    status = models.CharField(max_length=255)
