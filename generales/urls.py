from django.urls import include, path

from generales.views import Home, send_email

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('send_email', send_email, name='send_email'),
]
