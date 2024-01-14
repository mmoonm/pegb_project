from django.urls import path

from staff.modules.init_data.init_data.view import InitData

urlpatterns = [
    path('init/', InitData.as_view()),
]
