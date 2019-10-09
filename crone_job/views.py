from django.shortcuts import render, redirect
from .models import CronJob
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from passlib.hash import pbkdf2_sha256


# Landing page for login
def home(request):
	return render(request, 'home.html', {})


# Login existing user
def login_user(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, 'You have been logged in.')
			return redirect('crone')
		else:
			messages.error(request, 'Incorrect info.')
			return redirect('home')
	else:
		return render(request, 'login_user.html', {})


# Simple logout
def logout_user(request):
	logout(request)
	messages.success(request, 'You have been logout')
	return redirect('home')


# Create new user
def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, 'You have been registered...')
			return redirect('crone')
	else:
		form = SignUpForm()

	context = {'form': form}
	return render(request, 'register_user.html', context)


# Crone Job logic
def crone(request):
	if request.method == 'POST':
		title = request.POST.get('title')
		url = request.POST.get('url')

		http = request.POST.get('http')
		if http == 'on':
			http = True
		if http is None:
			http = False

		username = request.POST.get('username')

		password = request.POST.get('password')
		enc_password = pbkdf2_sha256.encrypt(password, rounds=12000, salt_size=32)

		all = request.POST.get('exampleRadios')
		allMinutes = request.POST.get("minutesAll")

		print('GANDALF = ', http, enc_password, all, allMinutes)

		'''if title:
            obj = CronJob.objects.create(title=title, url=url, http=http, username=username, password=password)
            obj.save()
            messages.success(request, 'You have been created new Crone...')'''
		return render(request, 'crone.html')
	else:
		return render(request, 'crone.html')
