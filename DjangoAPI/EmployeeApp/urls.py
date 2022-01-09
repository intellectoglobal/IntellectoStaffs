from django.conf.urls import url
from EmployeeApp import views

from django.conf.urls.static import static
from django.conf import settings


urlpatterns=[
    url(r'^companies$',views.companiesApi),
    url(r'^companies/([0-9]+)$',views.companiesApi),

    url(r'^employee$',views.employeeApi),
    url(r'^employee/([0-9]+)$',views.employeeApi)
    
]