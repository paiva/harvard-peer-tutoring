from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Course, Department, School
from .serializers import CourseSerializer
from django.http import HttpResponse


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
    
    html = ""
    all_departments = Department.objects.all()
    
    for d in all_departments:
    	url = '/search/' + str(d.id) + '/'
    	html += '<a href="' + url + '">' + d.department_name + '</a><br>'
    return HttpResponse(html)


def detail(request, course_id):
	return HttpResponse("<h2>Details for Department ID " + str(course_id) + "</h2>")


#def index(request):
#	return render(request, 'tutoring/home.html')

#def login(request):
#	return render(request, 'tutoring/login.html')

#def signup(request):
#	return render(request, 'tutoring/signup.html')

#def search(request):
#	return render(request, 'tutoring/search.html')