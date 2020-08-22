from django.shortcuts import render, redirect
from django.contrib.auth.models import User, AbstractUser 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import auth
from django.contrib.auth.models import User
from django.views.generic.detail import DetailView
from django.views import View
from .forms import UserCreationForm, ProfileForm
from .models import Profile


# Create your views here.

def signup(request):
    context=dict()
    if request.method == "POST":
        signup_form = UserCreationForm(request.POST)
        profile_form = ProfileForm(request.POST)
        
        if signup_form.is_valid() and profile_form.is_valid():
            signup_form.save()

            user = authenticate(request, username=signup_form.cleaned_data['username'], 
                                password =signup_form.cleaned_data['password1'])
            # if user:
            auth_login(request, user)
            
            get_profile = Profile.objects.get(id = user.profile.id)
            
            get_profile.nickname = profile_form.cleaned_data['nickname']
            get_profile.location = profile_form.cleaned_data['location']
            get_profile.age = profile_form.cleaned_data['age']

            get_profile.save()
            print('why')
            return redirect('index')

        else:
            context['user_form'] = signup_form
            return render(request,'signup.html', context)
            
    else:
        user_form = UserCreationForm()
        context['user_form'] = user_form

        context['profile_form'] =ProfileForm()
        
        return render(request,'signup.html', context)


def login(request):
    if request.method == "Post":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else :
            return render(request, 'registration/login.html', {'error': 'ID 혹은 비밀번호를 확인하세요.'})

    else :
        return render(request, 'registration/login.html')

    return render(request, 'registration/login.html')


def logout(request):
    auth.logout(request)
    return redirect('index')

def profile(request,pk):
    context=dict()
    profile_info = User.objects.get(id = pk)
    context['profile_info'] = profile_info
    return render(request,'profile.html',context)