from django.shortcuts import render,redirect
from dashboard.forms import workerForm, managerForm
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from .models import User_type
from django.contrib.auth.models import User


@login_required
def userLogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('userLogin'))

def registerWorker(request):
    registered=False
    if request.method=='POST':
        var_workerForm=workerForm(request.POST)
        if var_workerForm.is_valid():
            workerprimary=var_workerForm.save()
            workerprimary.set_password(workerprimary.password)
            workerprimary.save()
            registered=True
    else:
        var_workerForm=workerForm()
    return render(request,'dashboard/registerWorker.html',{'var_workerForm':var_workerForm,'registered':registered})


def registerManager(request):
    registered=False
    if request.method=='POST':
        var_managerForm=managerForm(request.POST)
        if var_managerForm.is_valid():
            managerprimary=var_managerForm.save()
            managerprimary.set_password(managerprimary.password)
            managerprimary.save()
            registered=True
    else:
        var_managerForm=managerForm()
    return render(request,'dashboard/registerManager.html',{'var_managerForm':var_managerForm,'registered':registered})

def userLogin(request):
    invalidlogin=False
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request, user)
            type_obj = User_type.objects.get(user=user)
            if user.is_authenticated and type_obj.is_worker:
                return redirect('workertDash') #Go to worker home
            elif user.is_authenticated and type_obj.is_manager:
                return redirect('managerDash') #Go to manager home
        else:
            # Invalid email or password. Handle as you wish
            return HttpResponse('<h1>Page was found</h1>')
            # return render(request, 'dashboard/login.html')
    return render(request, 'dashboard/login.html')



def workerDash(request):
    return render(request,'dashboard/workerDash.html')

def managerDash(request):
    return render(request,'dashboard/managerDash.html')