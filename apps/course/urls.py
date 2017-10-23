from django.conf.urls import url 
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'courses$', views.courses),
    url(r'courses/destroy/(?P<course_id>\d+)', views.destroy),
    url(r'courses/remove/(?P<course_id>\d+)', views.remove),
    url(r'courses/no', views.no),
    url(r'courses/add', views.add),
]