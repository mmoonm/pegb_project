__all__ = ["AddCustomerDiscount"]

from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from common.base.base_view import BaseAPIView
from rest_framework import serializers, status

from staff.modules.activities.add_customer_discount.dto import CustomerDiscountData
from staff.modules.activities.add_customer_discount.exceptions import CustomerLevelDoesNotExist, AddCustomerDiscountFail
from staff.modules.activities.add_customer_discount.service import AddCustomerDiscountService


class InputSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100, required=True)
    discount = serializers.IntegerField(max_value=100, required=True)


class AddCustomerDiscount(BaseAPIView):
    permission_classes = [IsAuthenticated]

    def __init__(self):
        super().__init__()
        self.service = AddCustomerDiscountService()

    def post(self, request: Request):
        input_data = InputSerializer(data=request.data)
        if input_data.is_valid() is not True:
            return JsonResponse({
                'message': 'Invalid param!'
            }, status=status.HTTP_400_BAD_REQUEST)

        discount_data = CustomerDiscountData(
            name=input_data.validated_data['name'],
            discount=input_data.validated_data['discount']
        )
        try:
            self.service.add_customer_discount(discount_data)
            return JsonResponse({
                'message': 'Add customer discount successful!'
            }, status=status.HTTP_201_CREATED)
        except CustomerLevelDoesNotExist:
            return JsonResponse({
                'message': 'Customer level does not exist!'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except AddCustomerDiscountFail:
            return JsonResponse({
                'message': 'Create customer discount fail'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
