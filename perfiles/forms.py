from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Perfil

class SignUpForm(UserCreationForm):
    username = forms.CharField(label='Usuario:', min_length=4, max_length=150,widget=forms.TextInput(attrs={'class': 'form-group valid-form has-error','placeholder': 'Escribir un usuario aquí'}))
    first_name = forms.CharField(forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}), max_length=32, help_text='First name')
    last_name=forms.CharField(forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}), max_length=32, help_text='Last name')
    email=forms.EmailField(forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}), max_length=64, help_text='Enter a valid email address')
    password1=forms.CharField(forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2=forms.CharField(forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password Again'}))

    class Meta:
        model = User
        # I've tried both of these 'fields' declaration, result is the same
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
        #fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email',)