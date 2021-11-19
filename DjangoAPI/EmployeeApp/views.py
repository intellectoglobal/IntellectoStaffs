from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from EmployeeApp.models import Companies, Employees
from EmployeeApp.serializers import CompaniesSerializer, EmployeeSerializer

from django.core.files.storage import default_storage

# Create your views here. 

@csrf_exempt  
def companiesApi(request,id=0):
    if request.method=='GET':
        companies = Companies.objects.all()
        companies_serializer = CompaniesSerializer(companies,many=True)
        return JsonResponse(companies_serializer.data,safe=False)
    elif request.method=='POST':
        companies_data = JSONParser().parse(request)
        companies_serializer=CompaniesSerializer(data=companies_data)
        if companies_serializer.is_valid():
            companies_serializer.save()
            return JsonResponse("Added Sucessfully",safe=False)
        return JsonResponse("failed to Add",safe=False)
    elif request.method=='PUT':
        companies_data=JSONParser().parse(request)  
        companies=Companies.objects.get(CompaniesId=companies_data['CompaniesId'])
        companies_serializer=CompaniesSerializer(companies,data=companies_data)
        if companies_serializer.is_valid():
            companies_serializer.save()
            return JsonResponse("Updated Scessfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        companies=Companies.objects.get(CompaniesId=id)
        companies.delete()
        return JsonResponse("Deleted Sucessesfully",safe=False)

@csrf_exempt  
def employeeApi(request,id=0):
    if request.method=='GET':
        employees = Employees.objects.all()
        employees_serializer = EmployeeSerializer(employees,many=True)
        return JsonResponse(employees_serializer.data,safe=False)
    elif request.method=='POST':
        employees_data = JSONParser().parse(request)
        employee_serializer=EmployeeSerializer(data=employees_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Added Sucessfully",safe=False)
        return JsonResponse("failed to Add",safe=False)
    elif request.method=='PUT':
        employee_data=JSONParser().parse(request)  
        employee=Employees.objects.get(EmployeeId=employee_data['EmployeeId'])
        employees_serializer=EmployeeSerializer(employee,data=employee_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Updated Scessfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        employee=Employees.objects.get(EmployeeId=id)
        employee.delete()
        return JsonResponse("Deleted Sucessesfully",safe=False)
                    
# @csrf_exempt
# def SaveFile(request):
#     file=request.FILES['file']
#     file_name=default_storage.save(file.name,file)
#     return JsonResponse(file_name,safe=False)
    


