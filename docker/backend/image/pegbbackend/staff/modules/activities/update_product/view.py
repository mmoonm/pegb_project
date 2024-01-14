__all__ = ["UpdateProduct"]

from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from common.base.base_view import BaseAPIView
from rest_framework import serializers, status

from staff.modules.activities.update_product.dto import ProductData
from staff.modules.activities.update_product.exceptions import DepartmentDoesNotExist, UpdateProductFail, \
    ProductDoesNotExist
from staff.modules.activities.update_product.service import UpdateProductService


class InputSerializer(serializers.Serializer):
    old_name = serializers.CharField(max_length=100, required=True)
    name = serializers.CharField(max_length=100, required=True)
    price = serializers.IntegerField(required=True)
    description = serializers.CharField(max_length=500, required=True)
    category = serializers.CharField(max_length=50, required=True)


class UpdateProduct(BaseAPIView):
    permission_classes = [IsAuthenticated]

    def __init__(self):
        super().__init__()
        self.service = UpdateProductService()

    def post(self, request: Request):
        input_data = InputSerializer(data=request.data)
        if input_data.is_valid() is not True:
            return JsonResponse({
                'message': 'Invalid param!'
            }, status=status.HTTP_400_BAD_REQUEST)

        product_data = ProductData(
            old_name=input_data.validated_data['old_name'],
            name=input_data.validated_data['name'],
            price=input_data.validated_data['price'],
            description=input_data.validated_data['description'],
            category=input_data.validated_data['category']
        )
        try:
            self.service.update_product(product_data)
            return JsonResponse({
                'message': 'Update product successful!'
            }, status=status.HTTP_201_CREATED)
        except DepartmentDoesNotExist:
            return JsonResponse({
                'message': 'Department does not exist!'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except UpdateProductFail:
            return JsonResponse({
                'message': 'Update product fail'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except ProductDoesNotExist:
            return JsonResponse({
                'message': 'Product does not exist'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
