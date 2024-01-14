from django.contrib.auth.hashers import make_password
from django.db import transaction
from django.http import JsonResponse
from rest_framework import serializers, status
from rest_framework.validators import UniqueValidator

from common.base.base_view import BaseAPIView
from common.models import Users, Staff, Department


class UserSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=Users.objects.all())])
    password = serializers.CharField(max_length=100, required=True)
    name = serializers.CharField(max_length=100, required=True)
    department = serializers.CharField(max_length=100, required=True)
    phone = serializers.CharField(max_length=20)

    class Meta:
        fields = ['email', 'password', 'name', 'department', 'phone']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        email = validated_data['email']
        password = validated_data['password']

        return Users.objects.create(email=email, password=password)


class UserSignUpView(BaseAPIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['password'] = make_password(serializer.validated_data['password'])

            try:
                with transaction.atomic():
                    user = serializer.save()

                    Staff.objects.create(
                        user=Users.objects.get(email=serializer.validated_data['email']),
                        name=serializer.validated_data['name'],
                        department=Department.objects.get(name=serializer.validated_data['department']),
                        phone=serializer.validated_data['phone'],)
            except:
                return JsonResponse({
                    'error_message': 'Invalid information',
                    'errors_code': 400,
                }, status=status.HTTP_503_SERVICE_UNAVAILABLE)

            return JsonResponse({
                'message': 'Register successful!'
            }, status=status.HTTP_201_CREATED)

        else:
            return JsonResponse({
                'error_message': 'Invalid information',
                'errors_code': 400,
            }, status=status.HTTP_400_BAD_REQUEST)
