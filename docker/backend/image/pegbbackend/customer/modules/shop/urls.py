from django.urls import path, include
from customer.modules.shop.add_to_cart.view import AddToCart
from customer.modules.shop.create_order.view import CreateOrder
from customer.modules.shop.get_list_order.view import GetListOrder
from customer.modules.shop.remove_from_cart.view import RemoveFromCart
from customer.modules.shop.get_list_in_cart.view import GetListInCart

urlpatterns = [
    path('add-to-cart/', AddToCart.as_view()),
    path('get-list-in-cart/', GetListInCart.as_view()),
    path('remove-from-cart/', RemoveFromCart.as_view()),
    path('create-order/', CreateOrder.as_view()),
    path('get-list-order/', GetListOrder.as_view()),
]
