from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Perfil

class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}), max_length=32, help_text='First name')
    last_name=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}), max_length=32, help_text='Last name')
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}), max_length=64, help_text='Enter a valid email address')
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password Again'}))

    class Meta(UserCreationForm.Meta):
        model = User
        # I've tried both of these 'fields' declaration, result is the same
        # fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email',)

#class SignUpForm(UserCreationForm):
#    #username = forms.CharField(label='Usuario:', min_length=4, max_length=150,widget=forms.TextInput(attrs={'class': 'form-group valid-form has-error','placeholder': 'Escribir un usuario aquí'}))
#    username = forms.CharField(label='Usuario:', min_length=4, max_length=150)
#    #first_name = forms.CharField(max_length=140, required=True, label= "Nombres:",widget=forms.TextInput(attrs={'class': 'form-group valid-form has-error','placeholder': 'Escriba sus nombres'}))
#    first_name = forms.CharField(max_length=140, required=True, label= "Nombres:")
#    #last_name = forms.CharField(max_length=140, required=False, label= "Apellidos:",widget=forms.TextInput(attrs={'class': 'form-group valid-form has-error','placeholder': 'Escriba sus Apellidos'}))
#    last_name = forms.CharField(max_length=140, required=False, label= "Apellidos:")
#    #email = forms.EmailField(required=True,widget=forms.TextInput(attrs={'class': 'form-group valid-form has-error','placeholder': 'Escriba una dirección de correo'}))
#    email = forms.EmailField(required=True)
#    #password1 = forms.CharField(label='Ingrese una clave:', widget=forms.PasswordInput, help_text  ="La clave debe al menos contener: Numero, Letra Mayúscula, Minúscula, caracter especial")
#    password1 = forms.CharField(label='Ingrese una clave:')
##    #password2 = forms.CharField(label='Repita la clave:', widget=forms.PasswordInput, help_text="Vuelva a ingresar su clave"),
 #   password2 = forms.CharField(label='Confirme la clave:')

#class Meta:
#        model = User
#        fields = ('username',
#                  'first_name',
#                  'last_name',
#                  'email',
#                  'password1',
#                  'password2',
#                  )
#        
#        labels = {
#            'username': 'Usuarios',
#            'first_name': 'Nombres',
#            'last_name': 'Apellidos',
#            'email': 'Correo Electronico',
#            'password1': 'Clave',
#            'password2': 'Clave',
#        }
    #fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email',)