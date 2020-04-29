from django.urls import path

from . import views

app_name = 'puesto'

urlpatterns = [
    path('', views.index_puesto, name='index'),
    path('create', views.create_puesto, name='create'),
    path('<int:puesto_id>/edit', views.edit_puesto, name='edit'),
    path('<int:puesto_id>/update', views.update_puesto, name='update'),
    path('store', views.store_puesto, name='store'),
    path('<int:puesto_id>/delete', views.delete_puesto, name='delete'),
]