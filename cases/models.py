# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime
# Create your models here.

class Cases(models.Model):
    description = models.CharField(max_length=1000)
    owner = models.CharField(max_length=20)
    case_typ = models.CharField(max_length=1000)
    date_added = models.DateField(default=datetime.datetime.now())
    # to show human readable data on the shell 
    def __str__(self):
     	  return self.description 