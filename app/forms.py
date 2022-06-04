from dataclasses import fields
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Image


class ImageForm(ModelForm):
   class Meta:
       model = Image
       fields = '__all__' 

    