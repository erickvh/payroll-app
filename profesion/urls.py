from django.urls import path

from . import views

app_name = 'profesion'

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('<int:profesion_id>/edit', views.edit, name='edit'),
    path('<int:profesion_id>/update', views.update, name='update'),
    path('store', views.store, name='store'),
]