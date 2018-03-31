from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.views.generic import CreateView, TemplateView
from django.views import generic

from .models import Perfil

from .forms import SignUpForm 
from django.views.generic.detail import DetailView
from perfiles.models import carreras, campus
from django.template.context_processors import request
from perfiles.forms import campusform, carrerasform, periodoslectivosform, estudiantesresumenform, asignaturasresumenform


class SignUpView(CreateView):
    model = Perfil
    #model = User
    
    template_name = 'perfiles/Registro.html'
    form_class = SignUpForm
    
    
    

def form_valid(self, form):
        '''
        En este parte, si el formulario es valido guardamos lo que se obtiene de él y usamos authenticate para que el usuario incie sesión luego de haberse registrado y lo redirigimos al index
        '''
        form.save()
        usuario = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        usuario = authenticate(username=usuario, password=password)
        login(self.request, usuario)
        return redirect('/')

class BienvenidaView(TemplateView):
   template_name = 'perfiles/index.html'
   
from django.contrib.auth.views import LoginView

class SignInView(LoginView):
    template_name = 'perfiles/iniciar_sesion.html'

from django.contrib.auth.views import LoginView, LogoutView 

class SignOutView(LogoutView):
    pass

#usando una vista basada en funcion
def campus_view(request):
    #model:campus
    if request.method == 'POST':
        form=campusform(request.POST)
        
        if form.is_valid():
            form.save()
        return redirect('bienvenida')
    
    else:
        form = campusform()
    return render (request,'perfiles/campus_form.html',{'form':form})

def carreras_view(request):
    #model:campus
    if request.method == 'POST':
        form=carrerasform(request.POST)
        
        if form.is_valid():
            form.save()
        return redirect('bienvenida')
    
    else:
        form = carrerasform()
    return render (request,'perfiles/carreras_form.html',{'form':form})


def periodoslectivos_view(request):
    #model:campus
    if request.method == 'POST':
        form=periodoslectivosform(request.POST)
        
        if form.is_valid():
            form.save()
        return redirect('bienvenida')
    
    else:
        form = periodoslectivosform()
    return render (request,'perfiles/periodoslectivos_form.html',{'form':form})


def estudiantesresumen_view(request):
    #model:campus
    if request.method == 'POST':
        form=estudiantesresumenform(request.POST)
        
        if form.is_valid():
            form.save()
        return redirect('bienvenida')
    
    else:
        form = estudiantesresumenform()
    return render (request,'perfiles/estudiantesresumen_form.html',{'form':form})

#asignaturasresumenform

def asignaturasresumen_view(request):
    #model:campus
    if request.method == 'POST':
        form=asignaturasresumenform(request.POST)
        
        if form.is_valid():
            form.save()
        return redirect('bienvenida')
    
    else:
        form = asignaturasresumenform()
    return render (request,'perfiles/asignaturasresumen_form.html',{'form':form})

class CampusVista (generic.ListView):
    model= campus
    template_name = 'perfiles/campus_list.html'   
    
    def get_queryset(self):
        queryset = campus.objects.all()
        return queryset
   

    
    
    
    
    
    
