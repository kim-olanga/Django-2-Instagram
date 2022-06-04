from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ImageForm, CreateUserForm

# Create your views here.
def signupPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request,'Account was created for '+ user)
                return redirect('login')

        context = {'form':form}
        return render(request,'accounts/signup.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request,username=username,password=password)

            if user is not None:
                login(request,user)
                return redirect('index')
            else:
                messages.info(request,'username or password is incorrect')


        context = {}
        return render(request,'accounts/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

login_required(login_url='login')
def index(request):
    return render(request,'index.html')

login_required(login_url='login')
def newPost(request):
    
    return render(request,'new-post.html')
