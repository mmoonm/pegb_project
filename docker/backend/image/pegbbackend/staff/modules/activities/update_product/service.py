__all__ = ['UpdateProductService']

from common.models import Department, Product
from staff.modules.activities.update_product.dto import ProductData
from staff.modules.activities.update_product.exceptions import DepartmentDoesNotExist, UpdateProductFail, \
    ProductDoesNotExist
import datetime

class UpdateProductService:

    def update_product(self, product_data: ProductData):
        try:
            product = Product.objects.get(name=product_data.old_name)
        except Exception as e:
            raise ProductDoesNotExist

        if not Department.objects.filter(name=product_data.category).exists():
            raise DepartmentDoesNotExist

        try:
            product.name = product_data.name
            product.price = product_data.price
            product.description = product_data.description
            product.category = Department.objects.get(name=product_data.category)
            product.save()

        except Exception as e:
            raise UpdateProductFail
