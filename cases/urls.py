from django.conf.urls import url
from .import views

app_name='cases'

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^register/$', views.register, name='register'),
	url(r'^login_user/$', views.login_user, name='login_user'),
	url(r'^addCases/$', views.addCases, name='addCases'),
	url(r'^logout_user/$', views.logout_user, name='logout_user'),
	url(r'^(?P<cases_id>[0-9]+)/delete_case/$', views.delete_case, name='delete_case'),
	url(r'^detail/$', views.detail, name='detail'),
]