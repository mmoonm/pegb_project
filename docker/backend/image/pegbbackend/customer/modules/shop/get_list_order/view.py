__all__ = ["GetListOrder"]

from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from common.base.base_view import BaseAPIView
from rest_framework import status

from common.models import Customer, Order
from customer.modules.shop.get_list_order.exceptions import GetListOrderFail


class GetListOrder(BaseAPIView):
    permission_classes = [IsAuthenticated]

    def __init__(self):
        super().__init__()

    def get(self, request: Request):

        try:
            customer = Customer.objects.get(user=request.user)
            order_list = Order.objects.filter(customer=customer).values('product__name',
                                                                        'product_amount',
                                                                        'amount',
                                                                        'discount',
                                                                        'order_datetime',)

            return JsonResponse(
                {
                    'data': list(order_list)
                },
                status=status.HTTP_200_OK)
        except GetListOrderFail:
            return JsonResponse({
                'message': 'Get list order fail'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
