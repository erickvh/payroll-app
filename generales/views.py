import os
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.core.mail import send_mail
from django.contrib import messages



# Create your views here.
class HomePage(generic.View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Pagina Inicio')


class Home(generic.TemplateView):
    template_name = 'home.html'


def send_email(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name', None)
        user_email = request.POST.get('user_email', None)
        user_rol = request.POST.get('user_rol', None)
        user_department = request.POST.get('user_department', None)
        subject = 'Solicitud {}'.format(user_name)
        body = 'Usuario: {} \n Email: {} \n Departamento: {} \n Rol: {}'.format(user_name, user_email, user_department,
                                                                                user_rol)
        # Send mail(Subject, body, from, to, fail)
        send_mail(subject, body,  os.getenv('EMAIL'), [os.getenv('EMAIL')], fail_silently=False)
        messages.success(request,'Solicitud enviada con exito')
        return render(request, 'send_email.html', {})
    return render(request, 'send_email.html', {})
