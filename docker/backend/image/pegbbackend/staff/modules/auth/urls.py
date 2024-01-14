from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView
from staff.modules.auth.signup.view import UserSignUpView

urlpatterns = [
    path('sign-up/', UserSignUpView.as_view()),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]
