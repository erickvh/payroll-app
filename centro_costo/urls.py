from django.urls import path

from . import views

app_name = 'centro_costo'

urlpatterns = [
    path('', views.index_centro_costos, name='index'),
    path('create', views.create_centro_costo, name='create'),
    path('store', views.store_centro_costo, name='store'),
    path('<int:centro_costo_id>/delete', views.delete_centro_costo, name='delete'),
    path('<int:centro_costo_id>/edit', views.edit_centro_costo, name='edit'),
    path('<int:centro_costo_id>/update', views.update_centro_costo, name='update'),
]
