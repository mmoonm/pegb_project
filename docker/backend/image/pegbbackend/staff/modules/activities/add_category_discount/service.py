__all__ = ['AddCategoryDiscountService']

from common.models import Department, Product, CustomerLevel
from staff.modules.activities.add_category_discount.dto import CategoryDiscountData
import datetime

from staff.modules.activities.add_category_discount.exceptions import DepartmentDoesNotExist, AddCategoryDiscountFail


class AddCategoryDiscountService:

    def add_category_discount(self, discount_data: CategoryDiscountData):
        if not Department.objects.filter(name=discount_data.name).exists():
            raise DepartmentDoesNotExist

        try:
            department = Department.objects.get(name=discount_data.name)
            department.discount = discount_data.discount
            department.save()

        except Exception as e:
            raise AddCategoryDiscountFail
