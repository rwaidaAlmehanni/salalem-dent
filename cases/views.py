# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template import loader
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse
#importing the cases model 
from .models import Cases

def index(request):
	template = loader.get_template('cases/index.html')
	context = {'all_cases':  Cases.objects.all()}
	# all_cases = Cases.objects.all()
	# html = ''
	# for case in all_cases:
	# 	url = '/cases/' + str(case.id)
	# 	html += '<a href="' + url + '">' + case.description + '</a><br>'
	return HttpResponse(template.render(context, request))

def detail(request, cases_id):
	try:
		case = Cases.objects.get(id=cases_id)
	except Cases.DoesNotExist:
		raise Http404('Cases Does not exist')
	return render(request, 'cases/detail.html', {'case':case})
