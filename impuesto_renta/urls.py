from django.urls import path

from . import views

app_name = 'renta'

urlpatterns = [
    path('', views.index_renta, name='index'),
    path('<int:renta_id>/edit', views.edit_renta, name='edit'),
    path('<int:renta_id>/update', views.update_renta, name='update')
]