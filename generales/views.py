import os
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.core.mail import send_mail


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
        send_mail(subject, body, os.getenv('EMAIL'), [os.getenv('EMAIL')], fail_silently=False)
        return render(request, 'send_email.html', {})
    return render(request, 'send_email.html', {})


def show_profile(request):
    user = request.user;
    if request.method == 'POST':
        current_password = request.POST.get('currentPassword', None)
        new_password = request.POST.get('newPassword', None)
        if user.check_password(current_password):
            user.set_password(new_password)
            user.save()
            message = 'Su Contraseña ha sido actualizada'
            return render(request, 'show_profile.html', {'user': user, 'message': message, 'codigo': 1})
        else:
            message = 'Debe digitar su contraseña actual'
            return render(request, 'show_profile.html', {'user': user, 'message': message, 'codigo': 2})
    return render(request, 'show_profile.html', {'user': user})
