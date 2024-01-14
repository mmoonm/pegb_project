__all__ = ["CreateOrder"]

from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from common.base.base_view import BaseAPIView
from rest_framework import status

from customer.modules.shop.create_order.exceptions import OrderFail
from customer.modules.shop.create_order.service import CreateOrderService


class CreateOrder(BaseAPIView):
    permission_classes = [IsAuthenticated]

    def __init__(self):
        super().__init__()
        self.service = CreateOrderService()

    def post(self, request: Request):
        email = request.user.email

        try:
            self.service.create_order(email)
            return JsonResponse({
                'message': 'create order successful!'
            }, status=status.HTTP_200_OK)

        except OrderFail:
            return JsonResponse({
                'message': 'Add product fail'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
