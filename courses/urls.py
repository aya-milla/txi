from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.CourseListView.as_view(), name='course_list'),

    url(r'^(?P<course_id>\d+)/$', views.detail, name='detail'),

    url(r'^create', views.create, name='create'),

    url(r'^edit/(?P<course_id>[0-9]+)/$', views.edit, name='edit'),

    url(r'^delete/(\d+)/$', views.delete, name='delete'),
    url(r'^(\d+)/delete/(\d+)/$', views.deleteTask, name='deleteTask'),
]
