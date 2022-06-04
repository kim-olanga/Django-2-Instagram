from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def loginPage(request):
    context = {}
    return render(request,'accounts/login.html', context)

def signupPage(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.Post)
        if form.is_valid():
            form.save()
            
    context = {'form':form}
    return render(request,'accounts/signup.html', context)

def index(request):
    return render(request,'index.html')

def newPost(request):
    return render(request,'new-post.html')
