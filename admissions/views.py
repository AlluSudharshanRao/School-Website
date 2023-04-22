import code
from django.shortcuts import render
from django.http import Http404, HttpResponse
from admissions.models import student

# Create your views here.


# function based views/class based views

# function based views


def homepage(request):
    return render(request,'index.html')

def addadmission(request):
    values={"name":"sudharshan", "age":20, "address":"Visakhapatnam"}
    return render(request,'admissions/addadmission.html',values)


def admissionsreport(request):
    #get all the records from the table
    result=student.objects.all(); #select * from students

    #store it in dictionary students
    students={'allstudents':result}
    return render(request,'admissions/admissionreport.html',students)