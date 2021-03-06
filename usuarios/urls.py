"""usuarios URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from perfiles.forms import campusform 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.urls import reverse

urlpatterns = [
    path('admin/', admin.site.urls),
]

from perfiles.views import SignUpView, BienvenidaView, InicioView, SignInView, SignOutView , CampusVista, campus_view, carreras_view, periodoslectivos_view, estudiantesresumen_view, asignaturasresumen_view, Resumen_Estudiantes_Vista, index

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^$', BienvenidaView.as_view(), name='bienvenida'),
    url(r'^$', InicioView.as_view(), name='inicio'),
    url(r'^inicio/$', InicioView.as_view(), name='inicio'),
    url(r'^estadistica/$', login_required(BienvenidaView.as_view()), name='bienvenida'),
    url(r'^registrate/$', SignUpView.as_view(), name='sign_up'),
    url(r'^inicia-sesion/$', SignInView.as_view(), name='sign_in'),
    #url(r'^inicia-sesion/$', login, {'template_name:iniciar_sesion.html'}, name='sign_in'),    
    url(r'^cerrar-sesion/$', SignOutView.as_view(), name='sign_out'),
    url(r'^campus-form/$', login_required(campus_view), name='campus_crear'),
    url(r'^campus-list/$', login_required(CampusVista.as_view()), name='campus_ver'),
    #url(r'^estudiantesresumen-list/$', Resumen_Estudiantes_Vista.as_view(), name='estudiantesresumen_ver'),
    url(r'^estudiantesresumen-list/$',index, name='estudiantesresumen_ver'),
    url(r'^carreras-form/$', login_required(carreras_view), name='carreras_crear'),
    url(r'^periodoslectivos-form/$', login_required(periodoslectivos_view), name='periodoslectivos_crear'),
    url(r'^estudiantesresumen-form/$', login_required(estudiantesresumen_view), name='estudiantesresumen_crear'),
    url(r'^asignaturasresumen-form/$', login_required(asignaturasresumen_view), name='asignaturasresumen_crear'),
    #asignaturasresumen_view
    #periodoslectivos
]


