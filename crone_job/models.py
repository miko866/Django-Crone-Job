"""
Create models for SQLite DB
"""
from django.db import models
# from passlib.hash import pbkdf2_sha256


class CronJob(models.Model):
	title = models.CharField(max_length=200, null=False, default='')
	url = models.URLField(max_length=250, null=False, default='')
	http = models.BooleanField(default=False, null=False)
	username = models.CharField(max_length=100, null=True, default='')
	password = models.CharField(max_length=255, null=True, default='')
	cron = models.CharField(max_length=255, null=False, default='')
	notification_jobs = models.BooleanField(default=False, null=True)
	notification_error = models.BooleanField(default=False, null=True)
	notification_deactivate = models.BooleanField(default=False, null=True)

	# Show in Django Admin string and not only Object
	def __str__(self):
		return self.title

	"""
	def verify_password(self, raw_password):
		return pbkdf2_sha256.verify(raw_password, self.password)
	"""
