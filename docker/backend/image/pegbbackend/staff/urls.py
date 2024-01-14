from django.urls import path, include
from staff.modules.auth import urls as authurls
from staff.modules.activities import urls as activitiesurls
from staff.modules.init_data import urls as initdataurls

urlpatterns = [
    path('auth/', include(authurls)),
    path('activities/', include(activitiesurls)),
    path('init-data/', include(initdataurls)),
]
