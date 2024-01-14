__all__ = ['RemoveProductService']

from common.models import Department, Product
from staff.modules.activities.add_product.dto import ProductData
from staff.modules.activities.add_product.exceptions import DepartmentDoesNotExist
import datetime

from staff.modules.activities.remove_product.exceptions import RemoveProductFail


class RemoveProductService:

    def remove_product(self, product_data: ProductData):
        if not Department.objects.filter(name=product_data.category).exists():
            raise DepartmentDoesNotExist
        else:
            try:
                product = Product.objects.get(
                    name=product_data.name,
                    description=product_data.description,
                    category=Department.objects.get(name=product_data.category),
                )
                product.delete()

            except Exception as e:
                print(e)
                raise RemoveProductFail





