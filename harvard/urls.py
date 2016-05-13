from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from search import views

urlpatterns = [
    url(r'^', include('search.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^search/', include('search.urls')),
    url(r'^api/', views.CourseList.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
