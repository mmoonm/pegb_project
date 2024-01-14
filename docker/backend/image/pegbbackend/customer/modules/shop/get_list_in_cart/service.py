__all__ = [
    "GetListInCartService"
]

from common.models import Users, Cart, Customer
from customer.modules.shop.get_list_in_cart.exceptions import GetListInCartFail


class GetListInCartService:

    def get_list(self, email: str):
        customer_user = Users.objects.get(email=email)
        try:
            cart = Cart.objects.filter(customer=Customer.objects.get(user=customer_user)).values('product__name', 'amount', 'product__price')
        except Exception as e:
            raise GetListInCartFail

        return list(cart)
