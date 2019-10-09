from django.shortcuts import render, redirect
from .models import CronJob
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm


def home(request):
    return render(request, 'home.html', {})


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
            messages.success(request, 'Incorrect info.')
            return redirect('home')
    else:
        return render(request, 'login_user.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logout')
    return redirect('home')


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
        all = request.POST.get('exampleRadios')
        allMinutes = request.POST.get("minutesAll")

        print('GANDALF = ', http, all, allMinutes)

        '''if title:
            obj = CronJob.objects.create(title=title, url=url, http=http, username=username, password=password)
            obj.save()
            messages.success(request, 'You have been created new Crone...')'''
        return render(request, 'crone.html')
    else:
        return render(request, 'crone.html')





