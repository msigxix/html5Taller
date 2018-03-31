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


urlpatterns = [
    path('admin/', admin.site.urls),
]

from perfiles.views import SignUpView, BienvenidaView, SignInView, SignOutView , CampusVista, campus_view, carreras_view, periodoslectivos_view, estudiantesresumen_view, asignaturasresumen_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', BienvenidaView.as_view(), name='bienvenida'),
    url(r'^registrate/$', SignUpView.as_view(template_name="Registro.html"), name='sign_up'),
    url(r'^inicia-sesion/$', SignInView.as_view(), name='sign_in'),
    url(r'^cerrar-sesion/$', SignOutView.as_view(), name='sign_out'),
    url(r'^campus-form/$', campus_view, name='campus_crear'),
    url(r'^campus-list/$', CampusVista.as_view(), name='campus_ver'),
    url(r'^carreras-form/$', carreras_view, name='carreras_crear'),
    url(r'^periodoslectivos-form/$', periodoslectivos_view, name='periodoslectivos_crear'),
    url(r'^estudiantesresumen-form/$', estudiantesresumen_view, name='estudiantesresumen_crear'),
    url(r'^asignaturasresumen-form/$', asignaturasresumen_view, name='asignaturasresumen_crear'),
    #asignaturasresumen_view
    #periodoslectivos
]


