# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


#table name will be post
class Post(models.Model):

	#these r the columns with the data type
	title= models.CharField(max_length=140)
	body=models.TextField()
	date=models.DateTimeField()

	def __str__(self):
		return self.title