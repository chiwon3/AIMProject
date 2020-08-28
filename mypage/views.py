from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .forms import Urlform1,Urlform2,Urlform3
from .models import CustomUrl1,CustomUrl2,CustomUrl3
from django.contrib.auth import get_user_model
from django.conf import settings
User = get_user_model()

# Create your views here.

def index(request): 
    custom_urls1 = CustomUrl1.objects.all()
    custom_urls2 = CustomUrl2.objects.all()
    custom_urls3 = CustomUrl3.objects.all()
    context = {}
    context['custom_urls1'] = custom_urls1
    context['custom_urls2'] = custom_urls2
    context['custom_urls3'] = custom_urls3
    return render(request, 'index_copy.html', context)


def create1(request,pk):
    context = dict()
    
    if request.method == "POST":
        temp_form = Urlform1(request.POST)
        if temp_form.is_valid():
            success_form = temp_form.save(commit=False)
            
            success_form.user = User.objects.get(id = pk)
            success_form.save()
            return redirect('index')
        else:
            context["temp_context"] = temp_form
            return render(request,'edit.html',context)
    else:
        context["temp_context"] = Urlform1()
        return render(request,'edit.html', context)


def update1(request,pk):
    context = dict()
    
    if request.method == "POST":
        temp_form = Urlform1(request.POST,instance=CustomUrl1.objects.get(id = pk))
        
        if temp_form.is_valid():
            temp_form.save()
            return redirect('index')
        else:
            context["temp_context"] = temp_form
            return render(request,'edit.html',context)
    else:
        context["temp_context"] = Urlform1(instance=CustomUrl1.objects.get(id = pk))
        return render(request,'edit.html', context)
