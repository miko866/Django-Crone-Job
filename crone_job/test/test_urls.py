from django.test import SimpleTestCase
from django.urls import reverse, resolve
from crone_job.views import home, login_user, register_user, logout_user, crone, entries


class TestUrls(SimpleTestCase):

	def test_home(self):
		url = reverse('home')
		self.assertEqual(resolve(url).func, home)

	def test_login_user(self):
		url = reverse('login')
		self.assertEqual(resolve(url).func, login_user)

	def test_register_user(self):
		url = reverse('register')
		self.assertEqual(resolve(url).func, register_user)

	def test_logout_user(self):
		url = reverse('logout')
		self.assertEqual(resolve(url).func, logout_user)

	def test_crone(self):
		url = reverse('crone')
		self.assertEqual(resolve(url).func, crone)

	def test_entries(self):
		url = reverse('entries')
		self.assertEqual(resolve(url).func, entries)
