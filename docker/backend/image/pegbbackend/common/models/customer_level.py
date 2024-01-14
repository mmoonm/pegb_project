from django.db import models


class CustomerLevel(models.Model):
    name = models.CharField(max_length=50)
    discount = models.IntegerField()
