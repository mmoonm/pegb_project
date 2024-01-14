__all__ = ["AddProduct"]

from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from common.base.base_view import BaseAPIView
from rest_framework import serializers, status

from staff.modules.activities.add_product.dto import ProductData
from staff.modules.activities.add_product.exceptions import DepartmentDoesNotExist, CreateProductFail
from staff.modules.activities.add_product.service import AddProductService


class InputSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100, required=True)
    price = serializers.IntegerField(required=True)
    description = serializers.CharField(max_length=500, required=True)
    category = serializers.CharField(max_length=50, required=True)


class AddProduct(BaseAPIView):
    permission_classes = [IsAuthenticated]

    def __init__(self):
        super().__init__()
        self.service = AddProductService()

    def post(self, request: Request):
        input_data = InputSerializer(data=request.data)
        if input_data.is_valid() is not True:
            return JsonResponse({
                'message': 'Invalid param!'
            }, status=status.HTTP_400_BAD_REQUEST)

        product_data = ProductData(
            name=input_data.validated_data['name'],
            price=input_data.validated_data['price'],
            description=input_data.validated_data['description'],
            category=input_data.validated_data['category']
        )
        try:
            self.service.add_product(product_data)
            return JsonResponse({
                'message': 'Add product successful!'
            }, status=status.HTTP_201_CREATED)
        except DepartmentDoesNotExist:
            return JsonResponse({
                'message': 'Department does not exist!'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except CreateProductFail:
            return JsonResponse({
                'message': 'Create product fail'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
