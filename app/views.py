from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Comment, Post,UserProfile
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import *

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
    current_user = request.user
    print(current_user)
    current_profile = UserProfile.objects.get(user_id=current_user)
    posts = Post.objects.all()[::-1]
    comments = Comment.objects.all()

    if request.method == "POST":
        post_form = PostForm(request.POST, request.FILES)

        if post_form.is_valid():
            post = post_form.save(commit=False)

            post.profile = current_user
            post.user_profile = current_profile

            post.save()
            post_form = PostForm()
            return HttpResponseRedirect(reverse("index"))

    else:
        post_form = PostForm()

    return render(request,'index.html')

def post(request, id):
    post = Post.objects.get(id = id)
    comments = Comment.objects.filter(post__id=id)
    current_user = request.user
    current_profile = UserProfile.objects.get(post=id)

    if request.method == "POST":
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = current_user
            comment.post = post
            comment.save()
            comment_form = CommentForm()
            return redirect("post", post.id)

    else:
        comment_form = CommentForm()

    return render(request, "post.html", context={"post":post,"current_user":current_user,"current_profile":current_profile,"comment_form":comment_form,"comments":comments,})
                                                          
def like(request, id):
    post = Post.objects.get(id = id)
    post.likes += 1
    post.save()
    return HttpResponseRedirect(reverse("index"))


def like_post(request, id):
    post = Post.objects.get(id = id)
    post.likes += 1
    post.save()
    return redirect("post", post.id)
                                                        
@login_required
def search(request):
    if 'profile' in request.GET and request.GET["profile"]:
        search_term = request.GET.get("profile")
        searched_user = UserProfile.search_by_user(search_term)
        message = f"{search_term}"
        user = User.objects.all()
        context = {
            "user":user,
            "message":message,
            "profile":searched_user
        }
        return render(request,'search_results.html',context)

    else:
        message = "You haven't searched for any term"
        return render(request, 'search_results.html',{"message":message})                                                        

@login_required
def profile(request, id):
    user = User.objects.get(id=id)
    profile = UserProfile.objects.get(user_id=user)
    posts = Post.objects.filter(profile__id=id)[::-1]
    return render(request, "profile.html", context={"user":user,"profile":profile,"posts":posts})
