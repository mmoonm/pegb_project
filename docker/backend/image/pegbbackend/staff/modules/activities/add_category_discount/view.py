__all__ = ["AddCategoryDiscount"]

from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from common.base.base_view import BaseAPIView
from rest_framework import serializers, status

from staff.modules.activities.add_category_discount.dto import CategoryDiscountData
from staff.modules.activities.add_category_discount.exceptions import DepartmentDoesNotExist, AddCategoryDiscountFail
from staff.modules.activities.add_category_discount.service import AddCategoryDiscountService


class InputSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100, required=True)
    discount = serializers.IntegerField(max_value=100, required=True)


class AddCategoryDiscount(BaseAPIView):
    permission_classes = [IsAuthenticated]

    def __init__(self):
        super().__init__()
        self.service = AddCategoryDiscountService()

    def post(self, request: Request):
        input_data = InputSerializer(data=request.data)
        if input_data.is_valid() is not True:
            return JsonResponse({
                'message': 'Invalid param!'
            }, status=status.HTTP_400_BAD_REQUEST)

        discount_data = CategoryDiscountData(
            name=input_data.validated_data['name'],
            discount=input_data.validated_data['discount']
        )
        try:
            self.service.add_category_discount(discount_data)
            return JsonResponse({
                'message': 'Add category discount successful!'
            }, status=status.HTTP_201_CREATED)
        except DepartmentDoesNotExist:
            return JsonResponse({
                'message': 'Department does not exist!'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except AddCategoryDiscountFail:
            return JsonResponse({
                'message': 'Create category discount fail'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
