from django.urls import include,path

from generales.views import Home

urlpatterns = [
    path('', Home.as_view(),name='home'),
]
