from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import campus 
from .models import Perfil
from .models import carreras, periodoslectivos
from blivetgui.dialogs import widgets
from django.forms import ModelForm
from django.contrib.contenttypes import fields
from pip._vendor.webencodings import labels

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



#class campusform (ModelForm):
class campusform (forms.ModelForm):
    class Meta:
        model=campus
        
        fields = [
                'id_campus',
                'cam_nombre',
                'cam_descripcion',
                'cam_longitud',
                'cam_latitud',
            ]
        
        labels = {
                'id_campus':'Codigo',
                'cam_nombre': 'Nombre de campus',
                'cam_descripcion': 'Descripcion',
                'cam_longitud': 'Longitud',
                'cam_latitud': 'Latitud',
            }
        widgets = {
                'cam_nombre': forms.TextInput(attrs={'class': 'form-control'}),
                'cam_descripcion': forms.TextInput(attrs={'class': 'form-control'}),
                'cam_longitud': forms.TextInput(attrs={'class': 'form-control'}),
                'cam_latitud': forms.TextInput(attrs={'class': 'form-control'}),
            }


class carrerasform (forms.ModelForm):

    class Meta:
        model = carreras
        fields = [
                'id_carrera',
                'car_nombre',
                'id_campus',
            ]
        labels = {
                'id_carrera':'Codigo',
                'car_nombre':'Nombre de la carrera',
                'id_campus' :'Id Campus',
            }
        widgets = {
            'car_nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'id_campus': forms.Select(attrs={'class': 'form-control'}),
            }

#periodoslectivos

class periodoslectivosform (forms.ModelForm):

    class Meta:
        model = periodoslectivos
        fields = [
                'id_periodo',
                'per_descripcion',
                
            ]
        labels = {
                'id_periodo':'Codigo Periodo',
                'per_descripcion':'Descripción Período',
                
            }
        widgets = {
            'id_periodo': forms.TextInput(attrs={'class': 'form-control'}),
            'per_descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            }  