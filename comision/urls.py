from django.urls import path

from . import views

app_name = 'comision'

urlpatterns = [
    path('', views.index_comision, name='index'),
    path('create', views.create_comision, name='create'),
    path('store', views.store_comision, name='store'),
    path('<int:comision_id>/edit', views.edit_comision, name='edit'),
    path('<int:comision_id>/update', views.update_comision, name='update'),
    path('<int:comision_id>/delete', views.delete_comision, name='delete'),
]