from django.db import models

# Create your models here.

class Companies(models.Model):
    CompaniesId = models.AutoField(primary_key=True)
    CompaniesName = models.CharField(max_length=500)

class Employees(models.Model):
    EmployeeId = models.AutoField(primary_key=True)
    EmployeeName = models.CharField(max_length=500)
    Department = models.CharField(max_length=500)
    DateOfJoining = models.DateField()
    Designation = models.CharField(max_length=500)
     