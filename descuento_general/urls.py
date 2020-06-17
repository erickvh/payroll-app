from django.urls import path

from . import views

app_name = 'descuento_general'

urlpatterns = [
    path('', views.descuento_ley, name='descuento_ley'),
    path('crear_descuento', views.crear_descuento, name='crear_descuento'),
    path('edit_descuento', views.edit_descuento, name='edit_descuento'),
    path('<int:descuento_id>/cerrar_descuento', views.cerrar_descuento, name='cerrar_descuento'),
#    path('<int:planilla_id>/show', views.show_planilla, name='show'),
]


