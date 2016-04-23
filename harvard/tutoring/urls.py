from django.conf.urls import include, url
from django.views.generic import TemplateView, RedirectView

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^tutoring/login/$', views.login, name='login'),
    

    #url(r'^$', TemplateView.as_view(template_name="home.html"), name='home'),
    url(r'^signup/$', TemplateView.as_view(template_name="signup.html"),
        name='signup'),
    url(r'^email-verification/$',
        TemplateView.as_view(template_name="email_verification.html"),
        name='email-verification'),
    #url(r'^login/$', TemplateView.as_view(template_name="login.html"),
    #    name='login'),
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

    url(r'^tutoring/search/$',TemplateView.as_view(template_name="tutoring/search.html"),name='search'),

    url(r'^tutoring/signup/$',
        TemplateView.as_view(template_name="tutoring/signup.html"),
        name='signup'),

    url(r'^favicon.ico/$', lambda x: HttpResponseRedirect(settings.STATIC_URL+'img/favicon.ico')),

]
