__all__ = ['AddCustomerDiscountService']

from common.models import CustomerLevel
from staff.modules.activities.add_customer_discount.exceptions import CustomerLevelDoesNotExist, AddCustomerDiscountFail
from staff.modules.activities.add_customer_discount.dto import CustomerDiscountData


class AddCustomerDiscountService:

    def add_customer_discount(self, discount_data: CustomerDiscountData):
        if not CustomerLevel.objects.filter(name=discount_data.name).exists():
            raise CustomerLevelDoesNotExist

        try:
            customer = CustomerLevel.objects.get(name=discount_data.name)
            customer.discount = discount_data.discount
            customer.save()

        except Exception as e:
            raise AddCustomerDiscountFail
