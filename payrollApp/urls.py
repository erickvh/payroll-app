"""payrollApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import include,path
from django.contrib.auth import views as auth_views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='login.html'),name='logout'),
    path('', include(('generales.urls','generales'),namespace = 'generales')),
    path('profesion/', include(('profesion.urls','profesion'), namespace = 'profesion')),
    path('estadocivil/', include(('estado_civil.urls','estadocivil'), namespace= 'estadocivil')),
    path('departamento/', include(('departamento.urls','departamento'), namespace= 'departamento')),
    path('tipounidad/', include(('tipo_unidad.urls','tipounidad'), namespace= 'tipounidad')),
    path('genero/', include(('genero.urls','genero'), namespace= 'genero')),
    path('puesto/', include(('puesto.urls','puesto'), namespace= 'puesto')),
    path('municipio/', include(('municipio.urls','municipio'), namespace= 'municipio')),
    path('unidad/', include(('unidad.urls','unidad'), namespace= 'unidad')),
    path('departamento_organizacion/', include(('departamento_organizacion.urls','departamento_organizacion'), namespace= 'departamento_organizacion')),
    path('centro_costo/', include(('centro_costo.urls', 'centro_costo'), namespace='centro_costo')),
    path('configuracion/', include(('configuracion.urls','configuracion'), namespace= 'configuracion'))
]
