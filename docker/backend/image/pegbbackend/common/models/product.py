from django.db import models

from common.models.department import Department


class Product(models.Model):
    name = models.CharField(max_length=50, unique=True)
    price = models.IntegerField()
    category = models.ForeignKey(Department, on_delete=models.CASCADE)
    description = models.CharField(max_length=50)
    created_date = models.DateField()
