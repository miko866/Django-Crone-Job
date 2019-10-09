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


# Cron Job logic
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

		crone_radios = request.POST.get('croneRadios')
		minutes_cron = request.POST.get("minutesCron")
		hours_day_cron = request.POST.get("hoursDayCron")
		minutes_day_cron = request.POST.get("minutesDayCron")
		month_always_cron = request.POST.get("monthAlwaysCron")
		hour_always_cron = request.POST.get("hourAlwaysCron")
		minutes_always_cron = request.POST.get("minutesAlwaysCron")
		user_def_cron = request.POST.get("userDefCron")
		notification_jobs = request.POST.get("notificationJobs")
		notification_error = request.POST.get("notificationError")
		notification_deactivate = request.POST.get("notificationDeactivate")

		if crone_radios:
			cron = (crone_radios, minutes_cron, hours_day_cron, month_always_cron, minutes_day_cron, hour_always_cron, minutes_always_cron)
			if minutes_cron != '00':
				int_minutes_cron = int(minutes_cron)
				int_minutes_cron -= 1
				minutes_cron = str(int_minutes_cron)

				list_minutes_cron = [minutes_cron, '*', '*', '*', '*']
				str_minutes_cron = ', '.join(list_minutes_cron)

				print('MINUTESCRON ', title, http, username, enc_password, str_minutes_cron)

			elif hours_day_cron != '00' and minutes_day_cron != '00':
				int_hours_day_cron = int(hours_day_cron)
				int_minutes_day_cron = int(minutes_day_cron)

				int_hours_day_cron -= 1
				int_minutes_day_cron -= 1

				hours_day_cron = str(int_hours_day_cron)
				minutes_day_cron = str(int_minutes_day_cron)

				list_day_cron = [minutes_day_cron, hours_day_cron, '*', '*', '*']
				str_day_cron = ', '.join(list_day_cron)

				print('DAYSCRON ', title, http, username, enc_password, str_day_cron)

			elif minutes_always_cron != '00' and hour_always_cron != '00' and month_always_cron != '00':

				int_minutes_always_croni = int(minutes_always_cron)
				int_hour_always_cron = int(hour_always_cron)
				int_month_always_cron = int(month_always_cron)

				int_minutes_always_croni -= 1
				int_hour_always_cron -= 1

				minutes_always_cron = str(int_minutes_always_croni)
				hour_always_cron = str(int_hour_always_cron)
				month_always_cron = str(int_month_always_cron)

				list_always_cron = [minutes_always_cron, hour_always_cron, month_always_cron, '*', '*']
				str_always_cron = ', '.join(list_always_cron)

				print('ALWAYSCRON ', title, http, username, enc_password,  str_always_cron)
			else:
				print('USERCRON ', title, http, username, enc_password, user_def_cron)

		# print('GANDALF = ', cron)

		'''
		if title:
            obj = CronJob.objects.create(title=title, url=url, http=http, username=username, password=password)
            obj.save()
            messages.success(request, 'You have been created new Crone...')
        '''
		return render(request, 'crone.html')
	else:
		return render(request, 'crone.html')
