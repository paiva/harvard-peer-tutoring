from django.views import generic
from .models import Course, Department, School

class IndexView(generic.ListView):
	template_name = 'search/home.html'
	context_object_name = 'object_list'


	def get_queryset(self):
		return Department.objects.all()


class DetailView(generic.DetailView):
	model = Department 
	template_name = 'search/detail.html'
