__all__ = ["InitData"]

from django.db import transaction
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from common.base.base_view import BaseAPIView
from rest_framework import serializers, status

from common.models import CustomerLevel, Department


class InitData(BaseAPIView):
    permission_classes = [IsAuthenticated]

    def __init__(self):
        super().__init__()

    def post(self, request: Request):

        customer_level_list = ['Bronze', 'Silver', 'Gold']
        department_list = ['pegb_group_A', 'pegb_group_B', 'pegb_group_C', 'pegb_group_D', 'pegb_group_E']
        try:
            with transaction.atomic():
                for item in customer_level_list:
                    if not CustomerLevel.objects.filter(name=item).exists():
                        CustomerLevel.objects.create(
                            name=item,
                            discount=0
                        )

                for item in department_list:
                    if not Department.objects.filter(name=item).exists():
                        Department.objects.create(
                            name=item,
                            discount=0
                        )

        except Exception as e:
            return JsonResponse({
                'message': e
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return JsonResponse({
            'message': 'Init data successful!'
        }, status=status.HTTP_201_CREATED)