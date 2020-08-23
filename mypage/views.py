from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .forms import Tabform
from .models import tab11

# Create your views here.

def index(request): 
    return render(request, 'index.html')

def edit_page(request,pk):
    context = dict()
    profile_info = User.objects.get(id = pk)
    if request.method == "POST":
        tab_form = Tabform(request.POST,instance=tab11.objects.get(id = request.user.id))
        if tab_form.is_valid():
            tab_form.save()
            return redirect('index')
        else:
            context["tab_form"] = tab_form
            return render(request,'edit.html',context)
    else:
        context["tab_form"] = Tabform(instance=tab11.objects.get(id = request.user.id))
        return render(request,'edit.html', context)