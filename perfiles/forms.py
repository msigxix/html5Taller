from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Perfil

class SignUpForm(UserCreationForm):
    username = forms.CharField(label='Usuario:', min_length=4, max_length=150,widget=forms.TextInput(attrs={'class': 'form-group valid-form has-error','placeholder': 'Escribir un usuario aquí'}))
    first_name = forms.CharField(max_length=140, required=True, label= "Nombres:",widget=forms.TextInput(attrs={'class': 'form-group valid-form has-error','placeholder': 'Escriba sus nombres'}))
    last_name = forms.CharField(max_length=140, required=False, label= "Apellidos:",widget=forms.TextInput(attrs={'class': 'form-group valid-form has-error','placeholder': 'Escriba sus Apellidos'}))
    email = forms.EmailField(required=True,widget=forms.TextInput(attrs={'class': 'form-group valid-form has-error','placeholder': 'Escriba una dirección de correo'}))
    password1 = forms.CharField(label='Ingrese una clave:', widget=forms.PasswordInput, help_text  ="La clave debe al menos contener: Numero, Letra Mayúscula, Minúscula, caracter especial")
    password2 = forms.CharField(label='Repita la clave:', widget=forms.PasswordInput, help_text="Vuelva a ingresar su clave"),

class Meta:
        model = User
        fields = ('username','email','first_name','last_name','password1','password2',)
        
        #labels = {
        #    'username': "Usuarios:",
        #    'email': "Correo Electronico",
        #    'first_name': "Nombre",
        #    'password1': "Clave",
        #}
    #fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email',)