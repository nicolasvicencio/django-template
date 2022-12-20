from django.shortcuts import render
from django.http import JsonResponse
from .models import Employee

# Create your views here.
def employeeView(request):
	emp={
		'id': 123,
		'name': 'Nicolas',
		'email': 'a@bx.cl',
		'salary': 5000
	}
	return JsonResponse(emp)


def employeesViewDB(request):
	employees = Employee.objects.all()
	data= {'Employees': list(employees.values('name', 'salary'))}
	return JsonResponse(data)
