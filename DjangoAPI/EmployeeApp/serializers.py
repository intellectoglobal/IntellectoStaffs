from django.db.models import fields
from rest_framework import serializers
from EmployeeApp.models import Companies,Employees

class CompaniesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Companies
        fields=('CompaniesId', 'CompaniesName')

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employees
        fields=('EmployeeId', 'EmployeeName', 'Department', 'DateOfJoining', 'Designation')
       