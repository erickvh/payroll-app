from django.urls import path

from . import views

app_name = 'usuario'

urlpatterns = [
    path('', views.index_usuario, name='index'),
    path('create', views.create_usuario, name='create'),
    # path('<int:puesto_id>/edit', views.edit_usuario, name='edit'),
    # path('<int:puesto_id>/update', views.update_usuario, name='update'),
    path('store', views.store_usuario, name='store'),
    # path('<int:puesto_id>/delete', views.toggle_usuario, name='toggle'),
    path('empleados/',views.get_employees_by_depto, name='list_empleados')
]