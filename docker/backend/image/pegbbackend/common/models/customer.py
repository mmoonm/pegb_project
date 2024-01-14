from django.db import models
from common.models.user import Users


class Customer(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    total_order = models.IntegerField()
