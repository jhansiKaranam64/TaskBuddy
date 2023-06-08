from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from django import forms 
from . models import Task
from django.core.exceptions import ValidationError
from django.utils import timezone


#-Registration form

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields =['username','email','password1','password2']

#-Login form

class LoginForm(AuthenticationForm):

    username =forms.CharField(widget=TextInput())
    password=forms.CharField(widget=PasswordInput())


#- Create a task

class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields =['title','content','due']
        exclude =['user',]
    '''def clean_due(self):
        due = self.cleaned_data['due']
        current_date = timezone.localdate()
        if due.date() < current_date:
            raise ValidationError("Due date must be in the future.")'''
        

#- Update a task

class UpdateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields =['title','content','due','completed']