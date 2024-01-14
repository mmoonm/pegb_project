__all__ = ["GetListProduct"]

from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from common.base.base_view import BaseAPIView
from rest_framework import status
from common.models import Product


class GetListProduct(BaseAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request: Request):
        department = list(Product.objects.values())
        return self._build_response(
            data=department,
            success=True,
            messages=status.HTTP_200_OK
        )
