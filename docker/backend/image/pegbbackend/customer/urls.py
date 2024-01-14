from django.urls import path, include
from customer.modules.auth import urls as authurls
from customer.modules.shop import urls as shopurls

urlpatterns = [
    path('auth/', include(authurls)),
    path('shop/', include(shopurls)),
]
