__all__ = ["GetListCategory"]

from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from common.base.base_view import BaseAPIView
from rest_framework import status
from common.models import Department


class GetListCategory(BaseAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request: Request):
        department = list(Department.objects.values())
        return self._build_response(
            data=department,
            success=True,
            messages=status.HTTP_200_OK
        )
