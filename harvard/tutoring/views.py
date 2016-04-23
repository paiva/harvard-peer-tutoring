from django.shortcuts import render
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