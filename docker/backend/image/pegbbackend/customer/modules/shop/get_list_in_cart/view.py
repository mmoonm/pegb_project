__all__ = ["GetListInCart"]

from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from common.base.base_view import BaseAPIView
from rest_framework import status
from common.models import Cart, Users
from customer.modules.shop.get_list_in_cart.exceptions import GetListInCartFail
from customer.modules.shop.get_list_in_cart.service import GetListInCartService


class GetListInCart(BaseAPIView):
    permission_classes = [IsAuthenticated]

    def __init__(self):
        super().__init__()
        self.service = GetListInCartService()

    def get(self, request: Request):

        email = request.user.email

        try:
            res_data = self.service.get_list(email)
            return JsonResponse(
                {
                    'data': res_data
                },
                status=status.HTTP_200_OK)
        except GetListInCartFail:
            return JsonResponse({
                'message': 'Get list in cart fail'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


