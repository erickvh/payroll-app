from django.urls import path

from . import views

app_name = 'genero'

urlpatterns = [
    path('', views.index_genero, name='index'),
    path('create', views.create_genero, name='create'),
    path('store', views.store_genero, name='store'),
    path('<int:genero_id>/edit', views.edit_genero, name='edit'),
    path('<int:genero_id>/update', views.update_genero, name='update'),
]