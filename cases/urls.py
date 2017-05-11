from django.conf.urls import url
from .import views




urlpatterns = [
	# Cases
    url(r'^$', views.index, name='index'),


    #/ Cases ID
    url(r'^(?P<cases_id>[0-9]+)$', views.case_detail, name='case_detail'),
]