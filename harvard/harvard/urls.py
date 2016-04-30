"""harvard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView, RedirectView
from rest_framework.urlpatterns import format_suffix_patterns
from tutoring import views

urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^courses/', views.CourseList.as_view()),


    url(r'^tutoring/', include('tutoring.urls')),



    url(r'^$', TemplateView.as_view(template_name="home.html"), name='home'),
    #url(r'^signup/$', TemplateView.as_view(template_name="signup.html"),
    #    name='signup'),
    url(r'^email-verification/$',
        TemplateView.as_view(template_name="email_verification.html"),
        name='email-verification'),
    url(r'^tutoring/login/$', TemplateView.as_view(template_name="tutoring/login.html"),
        name='login'),
    
    url(r'^logout/$', TemplateView.as_view(template_name="logout.html"),
        name='logout'),
    url(r'^password-reset/$',
        TemplateView.as_view(template_name="password_reset.html"),
        name='password-reset'),
    url(r'^password-reset/confirm/$',
        TemplateView.as_view(template_name="password_reset_confirm.html"),
        name='password-reset-confirm'),

    url(r'^user-details/$',
        TemplateView.as_view(template_name="user_details.html"),
        name='user-details'),
    url(r'^password-change/$',
        TemplateView.as_view(template_name="password_change.html"),
        name='password-change'),

    url(r'^tutoring/search$',TemplateView.as_view(template_name="tutoring/search.html"),name='search'),

    url(r'^tutoring/signup/$',
        TemplateView.as_view(template_name="tutoring/signup.html"),
        name='signup'),
]

urlpatterns = format_suffix_patterns(urlpatterns)