from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import StudentRegistration
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
# Create your views here.
def showformdata(request):
    if request.method=='POST':
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
        
            print('username:', fm.cleaned_data['username'])
            print('Email:',fm.cleaned_data['email'])
            print('address:',fm.cleaned_data['address'])
            
    

    else:
        fm=StudentRegistration()

    return render(request,'enroll/userregistration.html',{'form':fm})    


def user_login(request):
    if request.method=="POST":
        fm=AuthenticationForm(request=request,data=request.POST)
        if fm.is_valid():
            uname=fm.cleaned_data['username']
            upass=fm.cleaned_data['password']
            user=authenticate(username=uname, password=upass)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/profile/')

    else:            

        fm=AuthenticationForm()
    return render(request,'enroll/userlogin.html', {'form':fm})



def user_profile(request):
    return render(request,'enroll/profile.html')