from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from admissions.models import student

# Create your views here.

def feeCollection(request):
    return render(request,'accounts/feecollection.html')
    


def feeDuesReport(request):
    return  render(request,'accounts/feeduereport.html')


def feeCollectionReport(request):
    return  render(request,'accounts/feecollectionreport.html')