from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile, Post, Comment
from cloudinary.models import CloudinaryField


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ("profile_pic",)

class PostForm(forms.ModelForm):
    caption = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control",
                                                           "placeholder":"Caption...",
                                                           "rows":"4"}))
    image = CloudinaryField('image')

    class Meta:
        model = Post
        fields = ("caption", "image",) 

class CommentForm(forms.ModelForm):
    comment = forms.CharField(label=False, widget=forms.TextInput(attrs={"class":"form-control comment",
                                                                         "placeholder":"Add a comment..."}))

    class Meta:
        model = Comment
        fields = ("comment",)