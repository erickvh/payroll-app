from django.urls import path

from . import views

app_name = 'empleado'

urlpatterns = [
    path('', views.index_empleado, name='index'),
    #path('create', views.create_unidad, name='create'),
    #path('store', views.store_unidad, name='store'),
    #path('<int:unidad_id>/edit', views.edit_unidad, name='edit'),
    #path('<int:unidad_id>/update', views.update_unidad, name='update'),
    #path('<int:unidad_id>/delete', views.delete_unidad, name='delete')
]