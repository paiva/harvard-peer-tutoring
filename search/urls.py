from django.conf.urls import url
from . import views

app_name = 'search'

urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^(?P<department_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<course_id>[0-9]+)/request_tutor/$', views.request_tutor, name='request_tutor'),
    url(r'^courses/(?P<filter_by>[a-zA_Z]+)/$', views.courses, name='courses'),
]
