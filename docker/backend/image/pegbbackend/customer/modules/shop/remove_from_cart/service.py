__all__ = ['RemoveFromCartService']

from common.models import Product, Cart, Users, Customer
import datetime

from customer.modules.shop.remove_from_cart.exceptions import RemoveFromCartFail, ProductDoesNotExist


class RemoveFromCartService:

    def remove_from_cart(self, product_name: str, email: str):
        if not Product.objects.filter(name=product_name).exists():
            raise ProductDoesNotExist

        customer_user = Users.objects.get(email=email)

        if not Cart.objects.filter(customer=Customer.objects.get(user=customer_user),
                                   product=Product.objects.get(name=product_name)).exists():
            raise RemoveFromCartFail
        else:
            try:
                cart = Cart.objects.get(customer=Customer.objects.get(user=customer_user),
                                           product=Product.objects.get(name=product_name))
                new_amount = cart.amount - 1
                if new_amount == 0:
                    cart.delete()
                else:
                    cart.amount = new_amount
                    cart.save()

            except Exception as e:
                raise RemoveFromCartFail
