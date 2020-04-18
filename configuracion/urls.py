from django.urls import path

from . import views

app_name = 'configuracion'

urlpatterns = [
    path('', views.edit_configuracion, name='edit'),
    path('update', views.update_configuracion, name='update'),
]