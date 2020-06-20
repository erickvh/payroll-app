from django.urls import path
from . import views

app_name = 'usuario'

urlpatterns = [
    path('', views.index_usuario, name='index'),
    path('create', views.create_usuario, name='create'),
    path('<int:usuario_id>/edit', views.edit_usuario, name='edit'),
    path('<int:usuario_id>/update', views.update_usuario, name='update'),
    path('store', views.store_usuario, name='store'),
    path('<int:usuario_id>/toggle', views.toggle_usuario, name='toggle'),
    path('empleados/',views.get_employees_by_depto, name='list_empleados'),

    # Roles/Grupos
    path('index_rol/',views.index_rol, name='index_rol'),
    path('crear_rol/', views.crear_rol, name='crear_rol'),
    path('<int:group_id>/delete_rol', views.delete_rol, name='delete_rol'),

    # permisos
    path('index_permisos/',views.index_permisos, name='index_permisos'),
    path('<int:group_id>/permiso_rol/', views.permiso_rol, name='permiso_rol'),
    path('<int:permiso_id>/<int:group_id>/asignar_permiso/', views.asignar_permiso, name='asignar_permiso'),

    # roles    
    path('<int:user_id>/add_rol/', views.add_rol, name='add_rol'),
    path('<int:usuario_id>/<int:group_id>/asignar_rol/', views.asignar_rol, name='asignar_rol'),

    # menus
    path('index_menu/', views.index_menu, name='index_menu'),
    path('crear_menu/', views.crear_menu, name='crear_menu'),
    path('<int:menu_id>/delete_menu', views.delete_menu, name='delete_menu'),
    path('<int:group_id>/<int:menu_id>/asignar_menu/', views.asignar_menu, name='asignar_menu'),    
    path('<int:group_id>/add_menu/', views.add_menu, name='add_menu'),
    path('<int:group_id>/set_all_menu/', views.set_all_menu, name='set_all_menu'),
]



