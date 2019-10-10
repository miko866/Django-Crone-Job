from django.test import TestCase, Client
from django.urls import reverse
from crone_job.models import CronJob
import json


class TestViews(TestCase):

	def set_up(self):
		self.client = Client()
		self.list_url = reverse('crone')
		self.project1 = CronJob.objects.create(
			title='TestTitle',
			url='http://www.test.test'
		)

	def test_create_crone_POST(self):
		CronJob.objects.create(
			project=self.project1,
			title='TestIne'
		)

		response = self.client.post(self.list_url, {
			'title': 'Hallo',
			'name': 'Admin'
		})

		self.assertEqual(response.status_code, 302)
		self.assertEqual(self.project1.expenses.first().title, 'Hallo')











