from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import PredictResult

INPUT_CLASSES = 'form-control border'

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Your username',
        'class': 'm-1 p-1'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Your password',
        'class': 'm-1 p-1'
    }))
    
class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Your username',
        'class': 'm-1 p-1'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Your password',
        'class': 'm-1 p-1'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Repeat password',
        'class': 'm-1 p-1'
    }))

class NewItemForm(forms.ModelForm):
    class Meta:
        model = PredictResult
        fields = ('name','image')
    
        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES 
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES, 
            }),
        }