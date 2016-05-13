from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Course, Department, School
from .forms import UserForm
from .serializers import CourseSerializer

def index(request):
    if not request.user.is_authenticated():
        return render(request, 'search/login.html')
    else:
        departments = Department.objects.all()
        course_results = Course.objects.all()
        #query = request.GET.get("q")
        #if query:
        #    departments = departments.filter(
        #        Q(department_name__icontains=query) |
        #        Q(department_code__icontains=query)
        #    ).distinct()
        #    course_results = course_results.filter(
        #        Q(course_title__icontains=query)
        #    ).distinct()
        return render(request, 'search/index.html', {
                'departments': departments,
                'courses': course_results,
            })
        #else:
        #    return render(request, 'search/index.html', {'departments': departments})

def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'search/login.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                departments = Department.objects.filter()#(user=request.user)
                return render(request, 'search/index.html', {'departments': departments})
            else:
                return render(request, 'search/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'search/login.html', {'error_message': 'Invalid login'})
    return render(request, 'search/login.html')


def signup(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                departments = Department.objects.filter(user=request.user)
                return render(request, 'search/index.html', {'departments': departments})
    context = {
        "form": form,
    }
    return render(request, 'search/signup.html', context)



def detail(request, department_id):

    if not request.user.is_authenticated():
        return render(request, 'search/login.html')
    else:
        user = request.user
        department = get_object_or_404(Department, pk=department_id)
        return render(request, 'search/detail.html', {'department': department, 'user': user})


def request_tutor(request, course_id):
    course = get_object_or_404(course, pk=course_id)
    try:
        if course.has_tutor_request:
            course.has_tutor_request = False
        else:
            course.has_tutor_request = True
        course.save()
    except (KeyError, course.DoesNotExist):
        return JsonResponse({'success': False})
    else:
        return JsonResponse({'success': True})


def courses(request, filter_by):
    if not request.user.is_authenticated():
        return render(request, 'search/login.html')
    else:
        try:
            course_ids = []
            for department in Department.objects.filter(user=request.user):
                for course in department.course_set.all():
                    course_ids.append(course.pk)
            users_courses = Course.objects.filter(pk__in=course_ids)
            if filter_by == 'requests':
                users_courses = users_courses.filter(has_tutor_request=True)
        except department.DoesNotExist:
            users_courses = []
        return render(request, 'search/courses.html', {
            'course_list': users_courses,
            'filter_by': filter_by,
        })

class CourseList(APIView):

	def get(self,request):
		courses = Course.objects.all()
		serializer = CourseSerializer(courses,many=True)
		return Response(serializer.data)

	def post(self):
		pass
