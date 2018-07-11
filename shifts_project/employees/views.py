from django.shortcuts import render
from .models import Employee

def index(request):
  employees = Employee.objects.all()
  
  data = {
    'employees': employees
  }

  return render(request, 'employees/index.html', data)