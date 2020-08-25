from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .forms import Tabform
from .models import tab11,tab12,tab13,tab21,tab22,tab23,tab31,tab32,tab33

# Create your views here.

def index(request): 
    return render(request, 'index.html')


def create_page(request, pk):
    context = dict()
    profile_info = User.objects.get(id = pk)
    if request.method == "POST":
        user_tab_form = Tabform(request.POST)
        if user_tab_form.is_valid():
            success_form = user_tab_form.save(commit=False)
            
            success_form.author = User.objects.get(id = request.user.id)
            success_form.save()
            return redirect('index.html')
        else:
            context["tab_form"] = user_tab_form
            return render(request,'edit.html.',context)
    else:
        context["tab_form"] = Tabform()
        return render(request,'edit.html', context)


def edit_page_11(request, pk):
    context = dict()
    profile_info = User.objects.get(id = pk)
    if request.method == "POST":
        user_tab_form = Tabform(request.POST,instance=tab11.objects.get(id = request.user.id))
        if user_tab_form.is_valid():
            user_tab_form.save()
            return render(request, 'edit.html')
        else:
            context["tab_form"] = user_tab_form
            return render(request,'edit.html',context)
    else:
        context["tab_form"] = Tabform(instance=tab11.objects.get(id = request.user.id))
        return render(request,'edit.html', context)


def edit_page_12(request, pk):
    context = dict()
    profile_info = User.objects.get(id = pk)
    if request.method == "POST":
        user_tab_form = Tabform(request.POST,instance=tab12.objects.get(id = request.user.id))
        if user_tab_form.is_valid():
            user_tab_form.save()
            return render(request, 'edit.html')
        else:
            context["tab_form"] = user_tab_form
            return render(request,'edit.html',context)
    else:
        context["tab_form"] = Tabform(instance=tab12.objects.get(id = request.user.id))
        return render(request,'edit.html', context)


def edit_page_13(request, pk):
    context = dict()
    profile_info = User.objects.get(id = pk)
    if request.method == "POST":
        user_tab_form = Tabform(request.POST,instance=tab13.objects.get(id = request.user.id))
        if user_tab_form.is_valid():
            user_tab_form.save()
            return render(request, 'edit.html')
        else:
            context["tab_form"] = user_tab_form
            return render(request,'edit.html',context)
    else:
        context["tab_form"] = Tabform(instance=tab13.objects.get(id = request.user.id))
        return render(request,'edit.html', context)


def edit_page_21(request, pk):
    context = dict()
    profile_info = User.objects.get(id = pk)
    if request.method == "POST":
        user_tab_form = Tabform(request.POST,instance=tab21.objects.get(id = request.user.id))
        if user_tab_form.is_valid():
            user_tab_form.save()
            return render(request, 'edit.html')
        else:
            context["tab_form"] = user_tab_form
            return render(request,'edit.html',context)
    else:
        context["tab_form"] = Tabform(instance=tab21.objects.get(id = request.user.id))
        return render(request,'edit.html', context)


def edit_page_22(request, pk):
    context = dict()
    profile_info = User.objects.get(id = pk)
    if request.method == "POST":
        user_tab_form = Tabform(request.POST,instance=tab22.objects.get(id = request.user.id))
        if user_tab_form.is_valid():
            user_tab_form.save()
            return render(request, 'edit.html')
        else:
            context["tab_form"] = user_tab_form
            return render(request,'edit.html',context)
    else:
        context["tab_form"] = Tabform(instance=tab22.objects.get(id = request.user.id))
        return render(request,'edit.html', context)


def edit_page_23(request, pk):
    context = dict()
    profile_info = User.objects.get(id = pk)
    if request.method == "POST":
        user_tab_form = Tabform(request.POST,instance=tab23.objects.get(id = request.user.id))
        if user_tab_form.is_valid():
            user_tab_form.save()
            return render(request, 'edit.html')
        else:
            context["tab_form"] = user_tab_form
            return render(request,'edit.html',context)
    else:
        context["tab_form"] = Tabform(instance=tab23.objects.get(id = request.user.id))
        return render(request,'edit.html', context)


def edit_page_31(request, pk):
    context = dict()
    profile_info = User.objects.get(id = pk)
    if request.method == "POST":
        user_tab_form = Tabform(request.POST,instance=tab31.objects.get(id = request.user.id))
        if user_tab_form.is_valid():
            user_tab_form.save()
            return render(request, 'edit.html')
        else:
            context["tab_form"] = user_tab_form
            return render(request,'edit.html',context)
    else:
        context["tab_form"] = Tabform(instance=tab31.objects.get(id = request.user.id))
        return render(request,'edit.html', context)


def edit_page_32(request, pk):
    context = dict()
    profile_info = User.objects.get(id = pk)
    if request.method == "POST":
        user_tab_form = Tabform(request.POST,instance=tab32.objects.get(id = request.user.id))
        if user_tab_form.is_valid():
            user_tab_form.save()
            return render(request, 'edit.html')
        else:
            context["tab_form"] = user_tab_form
            return render(request,'edit.html',context)
    else:
        context["tab_form"] = Tabform(instance=tab32.objects.get(id = request.user.id))
        return render(request,'edit.html', context)


def edit_page_33(request, pk):
    context = dict()
    profile_info = User.objects.get(id = pk)
    if request.method == "POST":
        user_tab_form = Tabform(request.POST,instance=tab33.objects.get(id = request.user.id))
        if user_tab_form.is_valid():
            user_tab_form.save()
            return render(request, 'edit.html')
        else:
            context["tab_form"] = user_tab_form
            return render(request,'edit.html',context)
    else:
        context["tab_form"] = Tabform(instance=tab33.objects.get(id = request.user.id))
        return render(request,'edit.html', context)