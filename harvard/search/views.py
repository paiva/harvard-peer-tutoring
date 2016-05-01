from django.shortcuts import render, get_object_or_404
from django.template import loader
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Course, Department, School
from .serializers import CourseSerializer
from django.http import HttpResponse, Http404


# List all courses or create a new one
# Url: courses/CS50
class CourseList(APIView):
	# For get requests
	def get(self, request):
		courses = Course.objects.all()
		serlializer = CourseSerializer(courses, many=True)
		return Response(serlializer.data)

	# For post requests
	def post(self):
		pass


def index(request):
    
	all_departments = Department.objects.all()
	template = loader.get_template('search/search.html')	
	return render(request, 'search/search.html', { 'all_departments' : all_departments } )


def detail(request, department_id):
	try:
		department = Department.objects.get(pk=department_id)
	except Department.DoesNotExist:
		raise Http404("Department does not exist")
	return render(request, 'search/detail.html', { 'department' : department })


def add_couse(request):
	course = Course()

	course 	

def course_count_per_department(request, department):
	return department.course_set.count()

#def login(request):
#	return render(request, 'tutoring/login.html')

#def signup(request):
#	return render(request, 'tutoring/signup.html')

#def search(request):
#	return render(request, 'tutoring/search.html')