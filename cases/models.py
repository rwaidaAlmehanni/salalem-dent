# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Cases(models.Model):
    description = models.CharField(max_length=1000)
    
    # to show human readable data on the shell 
    def __str__(self):
     	  return self.description 