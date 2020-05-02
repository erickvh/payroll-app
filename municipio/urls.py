from django.urls import path

from . import views

app_name = 'municipio'

urlpatterns = [
    path('', views.index_municipio, name='index'),
    path('create', views.create_municipio, name='create'),
    path('store', views.store_municipio, name='store'),
    path('<int:municipio_id>/edit', views.edit_municipio, name='edit'),
    path('<int:municipio_id>/update', views.update_municipio, name='update'),
    path('<int:municipio_id>/delete', views.delete_municipio, name='delete')
]