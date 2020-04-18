from django.urls import path

from . import views

app_name = 'profesion'

urlpatterns = [
    path('', views.index_profesion, name='index'),
    path('create', views.create_profesion, name='create'),
    path('<int:profesion_id>/edit', views.edit_profesion, name='edit'),
    path('<int:profesion_id>/update', views.update_profesion, name='update'),
    path('store', views.store_profesion, name='store'),
]