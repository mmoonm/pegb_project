from django.db import models

from common.models.customer import Customer
from common.models.product import Product


class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    amount = models.IntegerField(default=1)
