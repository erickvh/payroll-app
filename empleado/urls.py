from django.urls import path
from django.conf.urls import url
from . import views

from .ajax import get_municipios

app_name = 'empleado'

urlpatterns = [
    path('', views.index_empleado, name='index'),
    path('create', views.create_empleado, name='create'),
    path('store', views.store_empleado, name='store'),
    url(r'^ajax/get_municipios/$', get_municipios, name='get_municipios'),
    path('<int:empleado_id>/show', views.show_empleado, name='show')
    #path('<int:unidad_id>/edit', views.edit_unidad, name='edit'),
    #path('<int:unidad_id>/update', views.update_unidad, name='update'),
    #path('<int:unidad_id>/delete', views.delete_unidad, name='delete')
]