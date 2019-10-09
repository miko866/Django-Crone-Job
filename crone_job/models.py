"""
Create models for SQLite DB
"""
from django.db import models


class CronJob(models.Model):
	title = models.CharField(max_length=200, null=False, default='')
	url = models.URLField(max_length=250, null=False, default='')
	http = models.BooleanField(default=False, null=False)
	username = models.CharField(max_length=100, null=True, default='')
	password = models.CharField(max_length=255, null=True, default='')

	# Show in Django Admin string and not only Object
	def __str__(self):
		return self.title
