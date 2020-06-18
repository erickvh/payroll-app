from django.urls import path

from . import views

app_name = 'descuento_general'

urlpatterns = [
    path('', views.descuento_ley, name='descuento_ley'),
    path('crear_descuento', views.crear_descuento, name='crear_descuento'),
    path('edit_descuento', views.edit_descuento, name='edit_descuento'),
    path('<int:descuento_id>/cerrar_descuento', views.cerrar_descuento, name='cerrar_descuento'),
 
    path('periodicidad', views.periodicidad, name='periodicidad'),
    path('crear_periodo', views.crear_periodo, name='crear_periodo'),
    path('<int:periodo_id>/cerrar_periodo', views.cerrar_periodo, name='cerrar_periodo'),

]


