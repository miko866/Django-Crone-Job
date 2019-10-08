from django.db import models
from django.contrib.auth.models import User


class CronJob(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=200, null=False, default='')
	url = models.URLField(max_length=250, null=False, default='')
	http = models.BooleanField(default=False)
	userweb = models.CharField(max_length=100, null=True, default='')

	def __str__(self):
		return self.title
