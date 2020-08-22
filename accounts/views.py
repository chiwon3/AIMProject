from django.shortcuts import render, redirect
from django.contrib.auth.models import User, AbstractUser 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
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
        Profile_form = ProfileForm(request.POST)

        if signup_form.is_valid() and Profile_form.is_valid():
            signup_form.save()

            user = authenticate(username=signup_form.cleaned_data['username'],
                                password=signup_form.cleaned_data['password1'])
            login(request,user)

            get_profile = Profile.objects.get(id = user.profile.id)

            get_profile.nickname = Profile_form.cleaned_data['nickname']
            get_profile.location = Profile_form.cleaned_data['location']
            get_profile.age = Profile_form.cleaned_data['age']

            tmp_profile.save()

            return redirect("index")

        else :
            print('work')
            context['signup_form'] = signup_form
    
            return render(request, 'signup.html',context)
            
    else : 
        signup_form = UserCreationForm()
        Profile_form = ProfileForm()

        context['signup_form'] = signup_form
        context['Profile_form'] = Profile_form
        
        return render(request, 'signup.html',context)


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

    return render(requset, 'registration/login.html')


def logout(request):
    auth.logout(request)
    return redirect('index')

def profile(request,pk):
    context=dict()
    profile_info = User.objects.get(id = pk)
    context['profile_info'] = profile_info
    return render(request,'profile.html',context)