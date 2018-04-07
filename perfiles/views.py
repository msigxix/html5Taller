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
from perfiles.models import carreras, campus, estudiantesresumen
from django.template.context_processors import request
from perfiles.forms import campusform, carrerasform, periodoslectivosform, estudiantesresumenform, asignaturasresumenform
from django.urls import reverse_lazy
import json as simplejson
from django.shortcuts import render_to_response
from django.forms.models import model_to_dict


class SignUpView(CreateView):
    model = Perfil
    #model = User
    
    template_name = 'perfiles/Registro.html'
    form_class = SignUpForm
    success_url = reverse_lazy('sign_in')
    
    

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

from perfiles.models import estudiantesresumen
from perfiles.models import asignaturasresumen

class BienvenidaView(TemplateView):
	template_name = 'perfiles/index.html'

	def get_context_data(self, **kwargs):
		context = super(BienvenidaView, self).get_context_data(**kwargs)
		context = self.cuadro1_informacion()
		#context = self.cuadro2_informacion()
		return context

	def cuadro1_informacion(self):
		datos1 = asignaturasresumen.objects.all()
		aprobados = []
		reprobados = []
		anulados=[]
		retiros=[]
		campus1=[]
		carrera1=[]
		#periodo=[]
		i = 0
		
		for item in datos1:
			aprobados.append(item.asi_aprobadas)
			reprobados.append(item.asi_reprobados)
			anulados.append(item.asi_anulados)
			retiros.append(item.asi_retiros)
			campus1.append(model_to_dict(item.id_campus))
			carrera1.append(model_to_dict(item.id_carrera))
			#periodo.append(model_to_dict(item.id_periodo))
            #campus.append(item.id_campus)
            #carrera.append(item.id_carrera)
            #periodo.append(item.id_periodo)
			i +=1
			
		aprobados=simplejson.dumps(aprobados)
		reprobados=simplejson.dumps(reprobados)
		anulados=simplejson.dumps(anulados)
		retiros=simplejson.dumps(retiros)
		campus1=simplejson.dumps(campus1)
		carrera1=simplejson.dumps(carrera1)
		#periodo=simplejson.dumps(periodo)
		#'periodo': periodo,
		
			
		
		
		datos3 = estudiantesresumen.objects.all()
		inscritos = []
		prematriculados = []
		matriculados=[]
		campus=[]
		carrera=[]
		#periodo=[]
		t = 0
		
		for item in datos3:
			inscritos.append(item.est_inscritos)
			prematriculados.append(item.est_prematriculados)
			matriculados.append(item.est_matriculados)
			campus.append(model_to_dict(item.id_campus))
			carrera.append(model_to_dict(item.id_carrera))
			#periodo.append(model_to_dict(item.id_periodo))
            #campus.append(item.id_campus)
            #carrera.append(item.id_carrera)
            #periodo.append(item.id_periodo)
			t +=1
			
		inscritos=simplejson.dumps(inscritos)
		prematriculados=simplejson.dumps(prematriculados)
		matriculados=simplejson.dumps(matriculados)
		campus=simplejson.dumps(campus)
		carrera=simplejson.dumps(carrera)
		#periodo=simplejson.dumps(periodo)
		#'periodo': periodo,
		info={
			'aprobados':aprobados,
            'reprobados':reprobados,
            'anulados':anulados,
			'retiros':retiros,
            'campus1':campus1,
            'carrera1': carrera1,
            'datos1': datos1,
            'i':i,
            #'fecha':fecha,
            'inscritos':inscritos,
            'prematriculados':prematriculados,
            'matriculados':matriculados,
            'campus':campus,
            'carrera': carrera,
            'datos3': datos3,
            't':t
        }
		
		return info
		
			

		
from django.contrib.auth.views import LoginView

class InicioView(TemplateView):
   template_name = 'perfiles/inicio.html'
   
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


class Resumen_Estudiantes_Vista (generic.ListView):
    #model= estudiantesresumen
    #template_name = 'perfiles/estudiantesresumen_list.html'   
    
    def get_queryset(self):
        queryset = estudiantesresumen.objects.all()
        return queryset
    

def index(request):
        datos = estudiantesresumen.objects.all()
        #datos_dict=model_to_dict(datos)
        inscritos = []
        prematriculados = []
        matriculados=[]
        campus=[]
        carrera=[]
        periodo=[]
        i = 0
        for item in datos:
            inscritos.append(item.est_inscritos)
            prematriculados.append(item.est_prematriculados)
            matriculados.append(item.est_matriculados)
            campus.append(model_to_dict(item.id_campus))
            carrera.append(model_to_dict(item.id_carrera))
            periodo.append(model_to_dict(item.id_periodo))
            #campus.append(item.id_campus)
            #carrera.append(item.id_carrera)
            #periodo.append(item.id_periodo)
            i +=1
    
        inscritos=simplejson.dumps(inscritos)
        prematriculados=simplejson.dumps(prematriculados)
        matriculados=simplejson.dumps(matriculados)
        campus=simplejson.dumps(campus)
        carrera=simplejson.dumps(carrera)
        periodo=simplejson.dumps(periodo)
        #fecha= date.today()
        context={
            #'fecha':fecha,
            'inscritos':inscritos,
            'prematriculados':prematriculados,
            'matriculados':matriculados,
            'campus':campus,
            'carrera': carrera,
            'periodo': periodo,
            'datos': datos,
            'i':i
        }
        return render_to_response('perfiles/estudiantesresumen_list.html',context)
    
    
    
    
    
    
