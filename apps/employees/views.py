from django.shortcuts import render

# Create your views here.
from .models import Employee
from rest_framework import viewsets
from .serializer import EmployeeSerializer

# Após o comentario "# Create your views here." e crie as views "Employee".

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer  