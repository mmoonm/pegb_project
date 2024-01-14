__all__ = ['AddProductService']

from common.models import Department, Product
from staff.modules.activities.add_product.dto import ProductData
from staff.modules.activities.add_product.exceptions import DepartmentDoesNotExist, CreateProductFail
import datetime


class AddProductService:

    def add_product(self, product_data: ProductData):
        if not Department.objects.filter(name=product_data.category).exists():
            raise DepartmentDoesNotExist
        else:
            try:
                Product.objects.create(
                    name=product_data.name,
                    price=product_data.price,
                    description=product_data.description,
                    category=Department.objects.get(name=product_data.category),
                    created_date=datetime.date.today()
                )

            except Exception as e:
                print(e)
                raise CreateProductFail





