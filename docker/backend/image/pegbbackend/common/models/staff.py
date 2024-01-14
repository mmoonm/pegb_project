from django.db import models

from common.models.department import Department
from common.models.user import Users


class Staff(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING)
