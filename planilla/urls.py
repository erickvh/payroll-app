from django.urls import path

from . import views

app_name = 'planilla'

urlpatterns = [
    path('', views.home, name='home'),
    path('create', views.create_planilla, name='create'),
    path('<int:planilla_id>/show', views.show_planilla, name='show'),
    path('<int:planilla_id>/close', views.close_planilla, name='close'),
    path('<int:empleado_id>/<int:planilla_id>/boleta', views.boleta, name='boleta'),
]