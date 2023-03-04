from django.shortcuts import redirect, render,get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from .models import Stake
from .forms import StakeForm
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'index.html')


def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')

    else:
        return render(request, 'login.html')



# @login_required(login_url='login')
def register_view(request):
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(request, username=username, password=password)
                login(request, user)
                return redirect('/')
        else:
            form = UserCreationForm()
        return render(request, 'register.html', {'form': form})


def logout(request):
    auth.logout(request)
    return redirect('/')




@csrf_exempt
def stake_create(request):
    if request.method == 'POST':
        form = StakeForm(request.POST)
        if form.is_valid():
            stake = form.save(commit=False)
            stake.investor_agent = request.user
            stake.save()
            return redirect('/')
    else:
        form = StakeForm()
    return render(request, 'stake_create.html', {'form': form})






