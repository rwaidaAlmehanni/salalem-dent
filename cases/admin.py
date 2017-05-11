# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
# importing Cases Model
from .models import Cases

# Register your models here.
admin.site.register(Cases)