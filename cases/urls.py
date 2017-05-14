from django.conf.urls import url
from .import views

app_name='cases'

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^register/$', views.register, name='register'),
	url(r'^login_user/$', views.login_user, name='login_user'),
	url(r'^addCases/$', views.addCases, name='addCases'),
	url(r'^logout_user/$', views.logout_user, name='logout_user'),
	url(r'^my_cases/$', views.my_cases, name='my_cases'),
	url(r'^(?P<cases_id>[0-9]+)/detail/$', views.detail, name='detail'),
	url(r'^(?P<cases_id>[0-9]+)/delete_cases/$', views.delete_cases, name='delete_cases'),
	url(r'^update_cases/$', views.update_cases, name='update_cases'),
	 
]
