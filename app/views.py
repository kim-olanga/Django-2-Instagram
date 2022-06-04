from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def loginPage(request):
    context = {}
    return render(request,'accounts/login.html', context)

def signupPage(request):
    form = UserCreationForm()
    context = {'form':form}
    return render(request,'accounts/signup.html', context)

def index(request):
    return render(request,'index.html')

def newPost(request):
    return render(request,'new-post.html')
