# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404,render,redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import JsonResponse
#imports del modelo
from usuario.models import User
from departamento_organizacion.models import DepartamentoOrganizacion
from empleado.models import Empleado
from .forms import UserForm
# Create your views here.
def index_usuario(request):
    usuarios = User.objects.all().order_by('username')
    return render(request, 'usuarios/index.html', {'usuario_list': usuarios})

def create_usuario(request):
    deptos=DepartamentoOrganizacion.objects.all().order_by('nombre')
    return render(request, 'usuarios/create.html',{'departamentos':deptos})

def get_employees_by_depto(request):
    departamento_id = request.GET.get('departamento_id')
    empleados = Empleado.objects.none()
    options = '<option value="" selected="selected">Seleccione un empleado</option>'
    if departamento_id:
        empleados = Empleado.objects.filter(departamento_organizacion_id=departamento_id)   
    for empleado in empleados:
        options += '<option value="%s">%s %s %s %s</option>' % (
            empleado.id,
            empleado.primer_nombre,
            empleado.segundo_nombre,
            empleado.apellido_paterno,
            empleado.apellido_materno

        )
    response = {}
    response['empleados'] = options
    return JsonResponse(response)

# def edit_puesto(request,puesto_id):
#     puesto = get_object_or_404(Puesto,pk=puesto_id)
#     return render(request, 'puesto/edit.html', {'puesto': puesto})

# def update_puesto(request, puesto_id):
#     puesto =  get_object_or_404(Puesto, pk=puesto_id)
#     if request.method == 'POST':
#         form = PuestoForm(request.POST, instance=puesto)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Puesto actualizado correctamente')
#         else:
#             errors=form.errors
#             return render(request, 'puesto/edit.html',{'errors': errors, 'puesto':puesto})
#     return redirect('/puesto')

def store_usuario(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=request.POST.get('username'),email=request.POST.get('email'),password=request.POST.get('password'))
            user.is_active=True
            user.is_superuser=form.cleaned_data['is_admin']
        
            if  form.cleaned_data['empleado']:
                user.first_name=form.cleaned_data.get('empleado').primer_nombre
                user.last_name=form.cleaned_data.get('empleado').apellido_paterno
     
            user.empleado=form.cleaned_data['empleado']
            user.save()
            messages.success(request, 'Puesto Guardado correctamente')
        else:
            errors=form.errors
            data=form.data
            deptos=DepartamentoOrganizacion.objects.all().order_by('nombre')
            print(data)
            return render(request, 'usuarios/create.html',{'errors': errors, 'data': data,'departamentos': deptos })
            
    return redirect('/usuarios')

# def delete_puesto(request, puesto_id):
#     puesto =  get_object_or_404(Puesto, pk=puesto_id)
#     puesto.delete()
#     messages.success(request, 'Puesto Borrado correctamente')

#     return redirect('/puesto')
