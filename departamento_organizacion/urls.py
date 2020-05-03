from django.urls import path

from . import views

app_name = 'departamento_organizacion'

urlpatterns = [
    path('', views.index_departamento_organizacion, name='index'),
    path('create', views.create_departamento_organizacion, name='create'),
    path('store', views.store_departamento_organizacion, name='store'),
    path('<int:departamento_id>/edit', views.edit_departamento_organizacion, name='edit'),
    path('<int:departamento_id>/update', views.update_departamento_organizacion, name='update'),
    path('<int:departamento_id>/delete', views.delete_departamento_organizacion, name='delete'),
]