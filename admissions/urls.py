from django.urls import path
from admissions.views import addadmission
from admissions.views import admissionsreport


urlpatterns = [
    path('newadm/',addadmission),
    path('admreport/',admissionsreport),
]