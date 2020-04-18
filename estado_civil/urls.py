from django.urls import path

from . import views

app_name = 'estadocivil'

urlpatterns = [
    path('', views.index_estado, name='index'),
    path('create', views.create_estado, name='create'),
    path('<int:estado_id>/edit', views.edit_estado, name='edit'),
    path('<int:estado_id>/update', views.update_estado, name='update'),
    path('store', views.store_estado, name='store'),
]