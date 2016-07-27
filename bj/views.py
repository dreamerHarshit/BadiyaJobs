from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Job_english,Company,Role,Job_hinglish,Job_hindi
from .serializers import Job_englishSerializer,CompanySerializer,RoleSerializer,Job_hinglishSerializer,Job_hindiSerializer 
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
# Create your views here.

class Job_englishList(APIView):
	def get(self, request):
		job=Job_english.objects.all()
		serializer=Job_englishSerializer(job, many=True)
		return Response(serializer.data)

class Job_hinglishList(APIView):
	def get(self, request):
		job=Job_hinglish.objects.all()
		serializer=Job_hinglishSerializer(job, many=True)
		return Response(serializer.data)

class Job_hindiList(APIView):
	def get(self, request):
		job=Job_hindi.objects.all()
		serializer=Job_hindiSerializer(job, many=True)
		return Response(serializer.data)

class RoleList(APIView):
	def get(self, request):
		role=Role.objects.all()
		serializer=RoleSerializer(role,many=True)
		return Response(serializer.data)

class CompanyList(APIView):
	def get(self, request):
		company=Company.objects.all()
		serializer=CompanySerializer(company,many=True)
		return Response(serializer.data)
