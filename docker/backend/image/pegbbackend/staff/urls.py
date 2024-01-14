from django.urls import path, include
from staff.modules.auth import urls as authurls
from staff.modules.activities import urls as activitiesurls

urlpatterns = [
    path('auth/', include(authurls)),
    path('activities/', include(activitiesurls)),
]
