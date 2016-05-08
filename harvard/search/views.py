from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .models import Course, Department, School
from .forms import UserForm

class IndexView(generic.ListView):
	template_name = 'search/home.html'
	context_object_name = 'object_list'


	def get_queryset(self):
		return Department.objects.all()


class DetailView(generic.DetailView):
	model = Department 
	template_name = 'search/detail.html'


class DepartmentCreate(CreateView):
	model = Department
	fields = ['department_name', 'department_code', 'department_logo']

class DepartmentUpdate(UpdateView):
	model = Department
	fields = ['department_name', 'department_code', 'department_logo']

class DepartmentDelete(DeleteView):
	model = Department
	success_url = reverse_lazy('search:index')

class UserFormView(View):
	form_class = UserForm
	template_name = 'search/signup.html'

	# Display blank form to the user
	def get(self,request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form':form})

	# Process form data
	def post(self,request):
		form = self.form_class(request.POST)

		if form.is_valid():

			user = form.save(commit=False)

			# Clean normalized data
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.set_password(password)
			user.save()

			# Returns User objects if credentials are correct
			user = autheticate(username=username, password=password)

			if user is not None:

				if user.is_active:
					login(request,user)
					return redirect('search:index')
		return render(request, self.template_name, {'form':form})



