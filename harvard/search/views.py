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
	department = get_object_or_404(Department, pk=department_id)
	return render(request, 'search/detail.html', { 'department' : department })


def tutors(request, department_id):
	department = get_object_or_404(Department, pk=department_id)

	# Try to get the selected song, else return error
	try:
		selected_course = department.course_set.get(pk=request.POST['course'])
	except (KeyError, course.DoesNotExist):
		return render(request, 'search/detail.html',
			{ 'department' : department,
			   'error' : 'You did not selected a valid course' })
	else:
		# Make changes in the database 
		selected_course.has_tutor_request = True
		selected_course.save()
		return render(request, 'search/detail.html', { 'department' : department })

def course_count_per_department(request, department):
	return department.course_set.count()

#def login(request):
#	return render(request, 'tutoring/login.html')

#def signup(request):
#	return render(request, 'tutoring/signup.html')

#def search(request):
#	return render(request, 'tutoring/search.html')