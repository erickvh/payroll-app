from django.urls import path

from . import views

app_name = 'departamento'

urlpatterns = [
    path('', views.index_departamento, name='index'),
    path('create', views.create_departamento, name='create'),
    path('<int:departamento_id>/edit', views.edit_departamento, name='edit'),
    path('<int:departamento_id>/update', views.update_departamento, name='update'),
    path('store', views.store_departamento, name='store'),
    path('<int:departamento_id>/delete', views.delete_departamento, name='delete'),
]