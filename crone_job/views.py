from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext

from .models import CronJob
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from passlib.hash import pbkdf2_sha256
from django.contrib.auth.decorators import login_required
import re


# Landing page for login
def home(request):
	return render(request, 'home.html', {})


# Login existing user
def login_user(request):
	# Listener for POST
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		# Check data from login form with DB
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, 'Sie sind eingeloggt. 🥳')
			return redirect('crone')
		else:
			messages.error(request, 'Falsche 👻.')
			return redirect('home')
	else:
		return render(request, 'login_user.html', {})


# Simple logout
def logout_user(request):
	logout(request)
	messages.success(request, 'Sie haben sich abgemeldet. 🦄 ')
	return redirect('home')


# Create new user
def register_user(request):
	# Listener for POST
	if request.method == 'POST':
		# Use forms.py
		form = SignUpForm(request.POST)
		# Check if is valid
		if form.is_valid():
			# Then save it wit control
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, 'Sie wurden registriert. 🦄 ')
			return redirect('crone')
	else:
		# Show only form
		form = SignUpForm()

	# Data from forms.py to FrontEnd
	context = {'form': form}
	return render(request, 'register_user.html', context)


# Decorator -> only logged user can that use
@login_required
# Cron Job logic
def crone(request):
	# Listener for POST
	if request.method == 'POST':
		# Take data from request

		author = request.user.username

		title = request.POST.get('title')
		url = request.POST.get('url')

		# Because Bootstrap checkbox :(
		http = request.POST.get('http')
		if http == 'on':
			http = True
		if http is None:
			http = False

		username = request.POST.get('username')

		# Hashed password
		password = request.POST.get('password')
		if password != '':
			enc_password = pbkdf2_sha256.encrypt(password, rounds=12000, salt_size=32)
		else:
			enc_password = ''

		# If checked can not empty
		if http:
			if username == '' and password == '':
				# If empty show Django message
				messages.error(request, 'Wenn HTTP aktiviert ist, dürfen Benutzername und Passwort nicht leer sein!')
				return render(request, 'crone.html')

		crone_radios = request.POST.get('croneRadios')
		minutes_cron = request.POST.get("minutesCron")
		hours_day_cron = request.POST.get("hoursDayCron")
		minutes_day_cron = request.POST.get("minutesDayCron")
		month_always_cron = request.POST.get("monthAlwaysCron")
		hour_always_cron = request.POST.get("hourAlwaysCron")
		minutes_always_cron = request.POST.get("minutesAlwaysCron")
		user_def_cron = request.POST.get("userDefCron")

		# Because Bootstrap checkbox :(
		notification_jobs = request.POST.get("notificationJobs")
		if notification_jobs == 'on':
			notification_jobs = True
		if notification_jobs is None:
			notification_jobs = False

		# Because Bootstrap checkbox :(
		notification_error = request.POST.get("notificationError")
		if notification_error == 'on':
			notification_error = True
		if notification_error is None:
			notification_error = False

		# Because Bootstrap checkbox :(
		notification_deactivate = request.POST.get("notificationDeactivate")
		if notification_deactivate == 'on':
			notification_deactivate = True
		if notification_deactivate is None:
			notification_deactivate = False

		# Because Bootstrap checkbox :(
		general_answer = request.POST.get("generalAnswer")
		if general_answer == 'on':
			general_answer = True
		if general_answer is None:
			general_answer = False

		# Logic for Cron-Job
		# Any radio checked show error message
		if crone_radios != '' and crone_radios is None:
			messages.error(request, 'Noo any Radios ... 😭')
			return render(request, 'crone.html')
		# Have one checked
		elif crone_radios:
			# If not only 00
			if minutes_cron != '00' and minutes_cron is not None:
				# Change to int and -1 because minutes start at 0
				int_minutes_cron = int(minutes_cron)
				int_minutes_cron -= 1
				minutes_cron = str(int_minutes_cron)

				# Make list and than string
				list_minutes_cron = [minutes_cron, '*', '*', '*', '*']
				str_minutes_cron = ', '.join(list_minutes_cron)

				print('MINUTESCRON ', title, url, http, username, enc_password, str_minutes_cron, notification_jobs,
					  notification_error, notification_deactivate, general_answer)

				# Save into DB
				obj = CronJob.objects.create(author=author, title=title, url=url, http=http, username=username, password=enc_password,
											 cron=str_minutes_cron, notification_jobs=notification_jobs,
											 notification_error=notification_error,
											 notification_deactivate=notification_deactivate,
											 general_answer=general_answer)
				obj.save()
				# If success show message
				messages.success(request, 'Es wurde ein neuer Cron-Job erstellt... 🎊 ')

			# If not only 00
			elif hours_day_cron != '00' and minutes_day_cron != '00' and hours_day_cron is not None and minutes_day_cron is not None:
				# Change to int and -1 because minutes and hours start at 0
				int_hours_day_cron = int(hours_day_cron)
				int_minutes_day_cron = int(minutes_day_cron)

				int_hours_day_cron -= 1
				int_minutes_day_cron -= 1

				hours_day_cron = str(int_hours_day_cron)
				minutes_day_cron = str(int_minutes_day_cron)

				# Make list and than string
				list_day_cron = [minutes_day_cron, hours_day_cron, '*', '*', '*']
				str_day_cron = ', '.join(list_day_cron)

				print('DAYSCRON ', title, url, http, username, enc_password, str_day_cron, notification_jobs,
					  notification_error, notification_deactivate, general_answer)

				# Save into DB
				obj = CronJob.objects.create(author=author, title=title, url=url, http=http, username=username, password=enc_password,
											 cron=str_day_cron, notification_jobs=notification_jobs,
											 notification_error=notification_error,
											 notification_deactivate=notification_deactivate,
											 general_answer=general_answer)
				obj.save()
				# If success show message
				messages.success(request, 'Es wurde ein neuer Cron-Job erstellt... 🎊 ')

			# If not only 00
			elif minutes_always_cron != '00' and hour_always_cron != '00' and month_always_cron != '00' and minutes_always_cron is not None and hour_always_cron is not None and month_always_cron is not None:
				# Change to int and -1 because minutes and hours start at 0
				int_minutes_always_croni = int(minutes_always_cron)
				int_hour_always_cron = int(hour_always_cron)
				int_month_always_cron = int(month_always_cron)

				int_minutes_always_croni -= 1
				int_hour_always_cron -= 1

				minutes_always_cron = str(int_minutes_always_croni)
				hour_always_cron = str(int_hour_always_cron)
				month_always_cron = str(int_month_always_cron)

				# Make list and than string
				list_always_cron = [minutes_always_cron, hour_always_cron, month_always_cron, '*', '*']
				str_always_cron = ', '.join(list_always_cron)

				print('ALWAYSCRON ', title, url, http, username, enc_password, str_always_cron, notification_jobs,
					  notification_error, notification_deactivate, general_answer)

				# Save into DB
				obj = CronJob.objects.create(author=author, title=title, url=url, http=http, username=username, password=enc_password,
											 cron=str_always_cron, notification_jobs=notification_jobs,
											 notification_error=notification_error,
											 notification_deactivate=notification_deactivate,
											 general_answer=general_answer)
				obj.save()
				# If success show message
				messages.success(request, 'Es wurde ein neuer Cron-Job erstellt... 🎊 ')
			else:
				# For User def. Cron
				"""print('USERCRON ', title, url, http, username, enc_password, user_def_cron, notification_jobs,
					  notification_error, notification_deactivate, general_answer)"""

				print('USER ', user_def_cron)

				if len(user_def_cron) > 5:
					# If too long show message and render
					messages.error(request,
								   'Ihr regulärer Ausdruck ist nicht korrekt!')
					return render(request, 'crone.html')

				# Check content with Regex
				reg_user_def_cron = re.search(r'\d[*]*', user_def_cron)

				# Save into DB
				obj = CronJob.objects.create(author=author, title=title, url=url, http=http, username=username, password=enc_password,
											 cron=reg_user_def_cron, notification_jobs=notification_jobs,
											 notification_error=notification_error,
											 notification_deactivate=notification_deactivate,
											 general_answer=general_answer)
				obj.save()
				# If success show message
				messages.success(request, 'Es wurde ein neuer Cron-Job erstellt... 🎊 ')

		# The stay here
		return render(request, 'crone.html')
	else:
		# Standard show Form
		return render(request, 'crone.html')


# Records
def entries(request):
	# Take all data from DB
	all_records = CronJob.objects.all
	# Send the Date into FrondEnd
	return render(request, 'entries.html', {'all_records': all_records})


# 404 work only DEBUG=False
def handler_404(request, exception):
	context = RequestContext(request)
	err_code = 404
	response = render_to_response('404.html', {"code": err_code}, context)
	response.status_code = 404
	return response
