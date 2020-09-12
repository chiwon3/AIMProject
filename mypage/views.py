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


# def create1(request,pk):
#     context = dict()
    
#     if request.method == "POST":
#         temp_form1 = Urlform1(request.POST)
#         temp_form2 = Urlform2(request.POST)
#         temp_form3 = Urlform3(request.POST)
#         if temp_form1.is_valid() or temp_form2.is_valid() or temp_form3.is_valid():
#             success_form1 = temp_form1.save(commit=False)
#             success_form2 = temp_form2.save(commit=False)
#             success_form3 = temp_form3.save(commit=False)
#             success_form1.user = User.objects.get(id = pk)
#             success_form2.user = User.objects.get(id = pk)
#             success_form3.user = User.objects.get(id = pk)
#             success_form1.save()
#             success_form2.save()
#             success_form3.save()
#             return redirect('index')
#         else:
#             context["temp_context1"] = temp_form1
#             context["temp_context2"] = temp_form2
#             context["temp_context3"] = temp_form3
#             return render(request,'edit.html',context)
#     else:
#         context["temp_context1"] = Urlform1()
#         context["temp_context2"] = Urlform2()
#         context["temp_context3"] = Urlform3()
#         return render(request,'edit.html', context)

def create1(request,pk):
    context = dict()
    
    if request.method == "POST":
        temp_form1 = Urlform1(request.POST)
        if temp_form1.is_valid():
            success_form1 = temp_form1.save(commit=False)
            success_form1.user = User.objects.get(id = pk)
            success_form1.save()
            return redirect('index')
        else:
            context["temp_context1"] = temp_form1
            return render(request,'edit.html',context)
    else:
        context["temp_context1"] = Urlform1()
        return render(request,'edit.html', context)

def create2(request,pk):
    context = dict()
    
    if request.method == "POST":
        temp_form2 = Urlform2(request.POST)
        if temp_form2.is_valid():
            success_form2 = temp_form2.save(commit=False)
            success_form2.user = User.objects.get(id = pk)
            success_form2.save()
            return redirect('index')
        else:
            context["temp_context1"] = temp_form2
            return render(request,'edit.html',context)
    else:
        context["temp_context2"] = Urlform2()
        return render(request,'edit.html', context)


def create3(request,pk):
    context = dict()
    
    if request.method == "POST":
        temp_form3 = Urlform3(request.POST)
        if temp_form3.is_valid():
            success_form3 = temp_form3.save(commit=False)
            success_form3.user = User.objects.get(id = pk)
            success_form3.save()
            return redirect('index')
        else:
            context["temp_context3"] = temp_form3
            return render(request,'edit.html',context)
    else:
        context["temp_context3"] = Urlform1()
        return render(request,'edit.html', context)

def update1(request,post_id):
    context = dict()
    
    if request.method == "POST":
        temp_form1 = Urlform1(request.POST,instance=CustomUrl1.objects.get(id = post_id))
        temp_form2 = Urlform2(request.POST,instance=CustomUrl2.objects.get(id = post_id))
        temp_form3 = Urlform3(request.POST,instance=CustomUrl3.objects.get(id = post_id))
        if temp_form1.is_valid():
            temp_form1.save()
            return redirect('index')
        
        elif temp_form2.is_valid():
            temp_form2.save()
            return redirect('index')
        
        elif temp_form3.is_valid():
            temp_form3.save()
            return redirect('index')
        else:
            context["temp_context1"] = temp_form1
            context["temp_context2"] = temp_form2
            context["temp_context3"] = temp_form3
            return render(request,'edit.html',context)
    else:
        context["temp_context1"] = Urlform1(instance=CustomUrl1.objects.get(id = post_id))
        context["temp_context2"] = Urlform2(instance=CustomUrl1.objects.get(id = post_id))
        context["temp_context3"] = Urlform3(instance=CustomUrl1.objects.get(id = post_id))
        return render(request,'edit.html', context)
