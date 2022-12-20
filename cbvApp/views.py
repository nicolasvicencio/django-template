from django.shortcuts import render
from .models import Student
from .serializer import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404

# Create your views here.
class StudentList(APIView):
	def get(self, request):
		students = Student.objects.all()
		ser = StudentSerializer(students, many=True)
		return Response(ser.data)
	
	def post(self, request):
		ser = StudentSerializer(data= request.data)
		if ser.is_valid():
			ser.save()
			return Response(ser.data, status=status.HTTP_201_CREATED)
		return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
	
class StudentDetails(APIView):
	def get_student(self, pk):
		try:
			return Student.objects.get(pk=pk)
		except Student.DoesNotExist:
			return Http404
		
	def get(self, request, pk):
		student = self.get_student(pk=pk)
		ser = StudentSerializer(student)
		return Response(ser.data)

	def put(self, request, pk):
		student = self.get_student(pk=pk)
		ser = StudentSerializer(student, data=request.data)
		if ser.is_valid():
			ser.save()
			return Response(ser.data)
		return Response(ser.errors, status=status.HTTP_404_NOT_FOUND)

	def delete(self, request,pk):
		student = self.get_student(pk=pk)
		student.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)