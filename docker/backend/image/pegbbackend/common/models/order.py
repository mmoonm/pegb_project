from django.db import models

from common.models.customer import Customer
from common.models.product import Product


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_id = models.IntegerField()
    product_amount = models.IntegerField()
    amount = models.IntegerField()
    discount = models.IntegerField()
    status = models.CharField(max_length=10)
    order_datetime = models.DateTimeField()
