from django.urls import path

from . import views

app_name = 'planilla'

urlpatterns = [
    path('', views.home, name='home'),
    path('create', views.create_planilla, name='create'),
    path('<int:planilla_id>/show', views.show_planilla, name='show'),
    path('<int:planilla_id>/close', views.close_planilla, name='close'),
    path('<int:empleado_id>/<int:planilla_id>/boleta', views.boleta, name='boleta'),
    path('nuevo_descuento', views.nuevo_descuento, name='nuevo_descuento'),
    path('<int:descuento_id>/delete_descuento', views.delete_descuento, name='delete_descuento'),
    path('nuevo_ingreso', views.nuevo_ingreso, name='nuevo_ingreso'),
    path('<int:ingreso_id>/delete_ingreso', views.delete_ingreso, name='delete_ingreso'),
]


