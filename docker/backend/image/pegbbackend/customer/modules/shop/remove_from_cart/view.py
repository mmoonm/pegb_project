__all__ = ["RemoveFromCart"]

from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from common.base.base_view import BaseAPIView
from rest_framework import serializers, status

from customer.modules.shop.remove_from_cart.exceptions import ProductDoesNotExist, RemoveFromCartFail
from customer.modules.shop.remove_from_cart.service import RemoveFromCartService


class InputSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100, required=True)

class RemoveFromCart(BaseAPIView):
    permission_classes = [IsAuthenticated]

    def __init__(self):
        super().__init__()
        self.service = RemoveFromCartService()

    def post(self, request: Request):
        input_data = InputSerializer(data=request.data)
        if input_data.is_valid() is not True:
            return JsonResponse({
                'message': 'Invalid param!'
            }, status=status.HTTP_400_BAD_REQUEST)

        email = request.user.email

        try:
            self.service.remove_from_cart(input_data.validated_data['name'], email)
            return JsonResponse({
                'message': 'Remove product from cart successful!'
            }, status=status.HTTP_200_OK)
        except ProductDoesNotExist:
            return JsonResponse({
                'message': 'Product does not exist!'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except RemoveFromCartFail:
            return JsonResponse({
                'message': 'Remove product fail'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
