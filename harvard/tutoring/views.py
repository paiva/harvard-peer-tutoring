from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIViews
from rest_framework.response import Response
from rest_framework import status
from .models import Course
from .serializers import CourseSerializer
from django.http import HttpResponse


#def index(request):
#    return HttpResponse("Hello, world. You're at the tutoring index.")

def index(request):
	return render(request, 'tutoring/home.html')

def login(request):
	return render(request, 'tutoring/login.html')

def signup(request):
	return render(request, 'tutoring/signup.html')

def search(request):
	return render(request, 'tutoring/search.html')