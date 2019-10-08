from django.shortcuts import render, redirect
from .models import CronJob
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
#from .forms import CronJobForm
from django.contrib.auth.models import User


def home(request):
	return render(request, 'home.html', {})


def login_user(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, ('You have been logged in.'))
			return redirect('crone')
		else:
			messages.success(request, ('Incorrect info.'))
			return redirect('home')
	else:
		return render(request, 'login_user.html', {})


def crone(request):
	#return render(request, 'crone.html', {})
	print('JASOM POST', request.POST)

	if request.method == 'POST':
		print(request.POST)
		title = request.POST.get('title')
		url = request.POST.get('url')
		http = request.POST.get('http')
		userweb = request.POST.get('userweb')

		if http == 'on':
			http = True

		if title:
			obj = CronJob.objects.create(title=title, url=url, http=http, userweb=userweb)
			print('JA som OBJECT', obj)
			obj.save()

		return render(request, 'crone.html')
	else:
		return render(request, 'crone.html')




