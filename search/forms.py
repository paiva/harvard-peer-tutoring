from django.contrib.auth.models import User
from django import forms

from .models import Course, Department, School

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ['username', 'email', 'password']

class DepartmentForm(forms.ModelForm):

    class Meta:
        model = Department
        fields = ['department_name', 'department_code', 'department_logo']

class CourseForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = ['course_code', 'course_name']
