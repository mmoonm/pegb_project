__all__ = ['BaseAPIView']

from rest_framework.views import APIView
from rest_framework.response import Response
import logging
from django.conf import settings


class BaseAPIView(APIView):
    def __init__(self, logger_name=None):
        super().__init__()

    @staticmethod
    def _build_response(success, data=None, errors=None, messages=None, response_code=None):
        response_data = {'success': success}

        if data is not None:
            response_data['data'] = data

        if errors is not None:
            response_data['errors'] = errors

        if messages is not None:
            response_data['messages'] = messages

        if response_code is not None:
            response_data['response_code'] = response_code

        return Response(response_data)