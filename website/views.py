from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages



# Create your views here.
def home(request):
    if request.method=='POST':
        user_name = request.POST['username']
        pass_word = request.POST['password']
        user_check = authenticate(request,username=user_name,password=pass_word)
        if user_check is not None:
            login(request,user_check)
            messages.success(request,"successfully loginned")
            return redirect('home')
        else:
            messages.success(request,"Incorrect username or password")
            return redirect('home')
    else:
        return render(request,'home.html',{})

def logout_user(request):
    logout(request)
    messages.success(request,"successfully loged out")
    return redirect('home')

def page1(request):
    return render(request,'page1.html',{})

