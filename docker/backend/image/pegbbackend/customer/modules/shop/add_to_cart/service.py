__all__ = ['AddToCartService']

from common.models import Product, Cart, Users, Customer
import datetime

from customer.modules.shop.add_to_cart.exceptions import ProductDoesNotExist, AddToCartFail


class AddToCartService:

    def add_to_cart(self, product_name: str, email: str):
        if not Product.objects.filter(name=product_name).exists():
            raise ProductDoesNotExist

        customer_user = Users.objects.get(email=email)

        if not Cart.objects.filter(customer=Customer.objects.get(user=customer_user),
                                   product=Product.objects.get(name=product_name)).exists():
            try:
                Cart.objects.create(
                    customer=Customer.objects.get(user=customer_user),
                    product=Product.objects.get(name=product_name),
                    amount=1
                )
            except Exception as e:
                raise AddToCartFail
        else:
            try:
                cart = Cart.objects.get(customer=Customer.objects.get(user=customer_user),
                                           product=Product.objects.get(name=product_name))
                new_amount = cart.amount + 1
                cart.amount = new_amount
                cart.save()
            except Exception as e:
                raise AddToCartFail
