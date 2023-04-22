from django.urls import path
from accounts.views import feeCollection
from accounts.views import feeCollectionReport
from accounts.views import feeDuesReport

urlpatterns = [

    path('feecoll/',feeCollection ),
    path('duesreport/',feeDuesReport ),
    path('collectionreport/',feeCollectionReport ),
]