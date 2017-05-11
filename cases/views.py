# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template import loader
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
#importing the cases model 
from .models import Cases

def index(request):
	all_cases = Cases.objects.all()
	template = loader.get_template('cases/index.html')
	context = {
		'all_cases': all_cases,
	}
	# all_cases = Cases.objects.all()
	# html = ''
	# for case in all_cases:
	# 	url = '/cases/' + str(case.id)
	# 	html += '<a href="' + url + '">' + case.description + '</a><br>'
	return HttpResponse(template.render(context, request))

def case_detail(request, cases_id):
	return HttpResponse("<h1>This is the case id :" + str(cases_id) + "</h2>")
