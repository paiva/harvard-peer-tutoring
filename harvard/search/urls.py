from django.conf.urls import include, url
from django.views.generic import TemplateView, RedirectView

from . import views


app_name = 'search'

urlpatterns = [
    
    # /search/
    url(r'^$', views.IndexView.as_view(), name='index'),
    
    # /signup/
    url(r'^signup/$', views.UserFormView.as_view(), name='signup'),

    # /search/department_id/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    
    # /search/department/add
    url(r'department/add/$', views.DepartmentCreate.as_view(), name='department-add'),

    # /search/department/2/
    url(r'department/(?P<pk>[0-9]+)/$', views.DepartmentUpdate.as_view(), name='department-update'),

    # /search/department/2/delete
    url(r'department/(?P<pk>[0-9]+)/delete/$', views.DepartmentDelete.as_view(), name='department-delete'),

]
