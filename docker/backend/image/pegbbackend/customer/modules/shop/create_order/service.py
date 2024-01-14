__all__ = ['CreateOrderService']

import pytz

from common.models import Users, Cart, Customer, CustomerLevel, Department, Order, Product
from customer.modules.shop.create_order.exceptions import OrderFail
from django.db import transaction
import datetime
from django.utils import timezone


class DiscountData:
    def __init__(self, product_category_discount, customer_level_discount):
        self.product_category_discount = product_category_discount
        self.customer_level_discount = customer_level_discount


class CreateOrderService:

    def create_order(self, email: str):
        customer_user = Users.objects.get(email=email)

        try:
            cart = Cart.objects.filter(customer=Customer.objects.get(user=customer_user)).values('product__name',
                                                                                                 'amount',
                                                                                                 'product__price',
                                                                                                 'product__category__discount')
            if not list(cart):
                raise OrderFail

            with transaction.atomic():
                customer_info = Customer.objects.get(user=customer_user)
                current_total_order = customer_info.total_order
                customer_level_discount = self.__get_customer_discount(current_total_order)

                for item in list(cart):
                    total_discount = item['amount'] * (
                                int(item['product__category__discount'] * item['product__price'] * 0.01) + int(
                            customer_level_discount * item['product__price'] * 0.01))

                    amount = (item['amount'] * item['product__price']) - total_discount

                    product = Product.objects.get(name=item['product__name'])

                    Order.objects.create(
                        customer=customer_info,
                        product=product,
                        order_id=current_total_order+1,
                        product_amount=item['amount'],
                        amount=amount,
                        discount=total_discount,
                        status='PENDING',
                        order_datetime=datetime.datetime.now(tz=pytz.utc)
                    )

                customer_info.total_order = current_total_order + 1
                customer_info.save()
        except Exception as e:
            print(e)
            raise OrderFail

    def __get_customer_discount(self, total_order):
        customer_level_info = CustomerLevel.objects.all()
        discount_info = {}

        if total_order < 21:
            customer_lever = 'Bronze'
        elif total_order < 50:
            customer_lever = 'Silver'
        else:
            customer_lever = 'Gold'

        for item in customer_level_info:
            discount_info[item.name] = item.discount

        return discount_info[customer_lever]

