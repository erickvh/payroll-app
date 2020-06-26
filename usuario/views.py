# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404,render,redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.contrib.auth.decorators import permission_required
from django.contrib.auth import authenticate, login

#imports del modelo
from usuario.models import User
from django.contrib.auth.models import Group, Permission
from departamento_organizacion.models import DepartamentoOrganizacion
from empleado.models import Empleado
from .forms import UserForm, UserUpdateForm
from django.contrib.auth.hashers import make_password
from .models import Menu
from generales.views import send_email_for_enable
import os

# Roles o grupos

def index_rol(request):
    groups = Group.objects.all()
    return render(request, 'usuarios/index_rol.html', {'groups':groups})

def crear_rol(request):
    if request.method == 'POST':
        rol = request.POST.get('rol', None)
        if rol:
            group = Group(name = rol)
            group.save()
            messages.success(request, 'Rol/grupo creado correctamente')
        else: 
            messages.error(request, 'Debe llenar todos los campos')
    return redirect('/usuarios/index_rol/')

def delete_rol(request, group_id):
    if request.method == 'POST':
        group = get_object_or_404(Group, pk=group_id)
        users = User.objects.filter(groups__name=group.name).exists()
        if not users:
            group.delete()
            messages.success(request, 'Rol/grupo eliminado correctamente')
        else:
            messages.error(request, 'Rol/grupo no se puede eliminar, hay usuarios asociados')
    return redirect('/usuarios/index_rol/')

# permisos
def index_permisos(request):
    permisos = Permission.objects.all()
    messages.success(request, 'Los permisos se agregan automaticamente, no puedes eliminarlos ni editarlos')
    return render(request, 'usuarios/index_permisos.html', {'permisos':permisos})

# Agregar permisos a roles
def permiso_rol(request, group_id):
    group = get_object_or_404(Group, pk=group_id)
    permisos = Permission.objects.exclude(group=group)
    mis_permisos = Permission.objects.filter(group=group)
    return render(request, 'usuarios/permiso_rol.html', {'permisos':permisos, 'mis_permisos':mis_permisos, 'group':group})

def asignar_permiso(request, permiso_id, group_id):
    group = get_object_or_404(Group, pk=group_id)
    permiso = get_object_or_404(Permission, pk=permiso_id)
    if request.method == 'POST':
        id_permiso = request.POST.get('id_permiso', None)
        if id_permiso == 'agregar':
            group.permissions.add(permiso)
            group.save()
        elif id_permiso == 'eliminar':
            group.permissions.remove(permiso)
            group.save()
    mis_permisos = Permission.objects.filter(group=group)
    return redirect('/usuarios/'+str(group_id)+'/permiso_rol/')

# agregar roles a usuario
def add_rol(request, user_id):
    usuario = get_object_or_404(User, pk=user_id)
    groups = Group.objects.exclude(user=usuario)
    mis_groups = Group.objects.filter(user=usuario)
    return render(request, 'usuarios/add_rol.html', {'groups':groups, 'mis_groups':mis_groups, 'usuario':usuario})

def asignar_rol(request, usuario_id, group_id):
    group = get_object_or_404(Group, pk=group_id)
    user = get_object_or_404(User, pk=usuario_id)
    if request.method == 'POST':
        id_permiso = request.POST.get('id_permiso', None)
        if id_permiso == 'agregar':
            user.groups.add(group)
            user.save()
        elif id_permiso == 'eliminar':
            user.groups.remove(group)
            user.save()
    return redirect('/usuarios/'+str(user.id)+'/add_rol/')

# menus
def index_menu(request):
    menu_list = Menu.objects.filter(padre=None)
    menus = Menu.objects.all()
    return render(request, 'usuarios/index_menu.html', {'menu_list':menu_list, 'menus':menus})

def crear_menu(request):
    if request.method == 'POST':
        menu_padre = int(request.POST.get('menu_padre', 0))
        nombre = request.POST.get('nombre', None)
        url = request.POST.get('url', None)
        if menu_padre > 0 and nombre and url:
            padre = get_object_or_404(Menu, pk=menu_padre)
            menu = Menu(nombre=nombre, padre=padre, url= url)
            menu.save()
            messages.success(request, 'Submenu creado con exito')
        elif menu_padre == 0 and nombre:
            menu = Menu(nombre=nombre)
            menu.save()
            messages.success(request, 'Menu padre creado con exito')
        else:
            messages.error(request, 'No se pudo crear un nuevo menu')
    return redirect('/usuarios/index_menu/')

def delete_menu(request, menu_id):
    if request.method == 'POST':
        try:
            menu = get_object_or_404(Menu, pk=menu_id)
            if menu.groups.count() < 1:
                menu.delete()
                messages.success(request, 'Menu eliminado correctamente')
            else:
                messages.error(request, 'Menu no se puede eliminar, hay roles asociados')
        except:
            messages.error(request, 'No puedes eliminar un menu padre sin eliminar antes los hijos')
    return redirect('/usuarios/index_menu/')

def add_menu(request, group_id):
    group = get_object_or_404(Group, pk=group_id)
    menus = Menu.objects.filter(padre=None).exclude(groups=group)
    mis_menus = Menu.objects.filter(groups=group)
    return render(request, 'usuarios/add_menu.html', {'menus':menus, 'mis_menus':mis_menus, 'group':group})


def asignar_menu(request, group_id, menu_id):
    group = get_object_or_404(Group, pk=group_id)
    menu = get_object_or_404(Menu, pk=menu_id)
    if request.method == 'POST':
        id_permiso = request.POST.get('id_permiso', None)
        if id_permiso == 'agregar':
            menu.groups.add(group)
            menu.save()
        elif id_permiso == 'eliminar':
            menu.groups.remove(group)
            menu.save()
    return redirect('/usuarios/'+str(group_id)+'/add_menu/')


def set_all_menu(request, group_id):
    group = get_object_or_404(Group, pk=group_id)
    menus = Menu.objects.filter(padre=None)
    if request.method == 'POST':
        id_permiso = request.POST.get('id_permiso', None)
        if id_permiso == 'agregar':
            for menu in menus:
                menu.groups.add(group)
                menu.save()
        elif id_permiso == 'eliminar':
            for menu in menus:
                menu.groups.remove(group)
                menu.save()
    return redirect('/usuarios/'+str(group_id)+'/add_menu/')


# Usuarios
@permission_required('view_user')
def index_usuario(request):
    usuarios = User.objects.all().exclude(id=request.user.id).order_by('username')
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

def edit_usuario(request,usuario_id):
    usuario = get_object_or_404(User,pk=usuario_id)
    return render(request, 'usuarios/edit.html', {'usuario': usuario})

def update_usuario(request, usuario_id):
    usuario =  get_object_or_404(User, pk=usuario_id)
    if request.method == 'POST':
        form = UserUpdateForm(request.POST)
        if form.is_valid():
            pswd=form.cleaned_data.get('password')

            if(pswd):
                usuario.password=make_password(pswd)
            usuario.email=form.cleaned_data.get('email')
            usuario.is_superuser=form.cleaned_data.get('is_admin')
            usuario.save()
            messages.success(request, 'Usuario actualizado correctamente')
        else:
            errors=form.errors
            return render(request, 'usuarios/edit.html',{'errors': errors, 'usuario':usuario})
    return redirect('/usuarios')

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
            messages.success(request, 'Usuario Guardado correctamente')
        else:
            errors=form.errors
            data=form.data
            deptos=DepartamentoOrganizacion.objects.all().order_by('nombre')
            print(data)
            return render(request, 'usuarios/create.html',{'errors': errors, 'data': data,'departamentos': deptos })
            
    return redirect('/usuarios')

def toggle_usuario(request,usuario_id):
    usuario =  get_object_or_404(User, pk=usuario_id)
    usuario.is_active=not usuario.is_active
    usuario.save()
    if(usuario.is_active):
        message='Usuario {} esta activo'.format(usuario.username)
        messages.success(request, message)
    else:
        message='Usuario {} desactivado'.format(usuario.username)
        messages.warning(request, message)

    return redirect('/usuarios')


def servicio_validacion(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        if username and password:
            usuario = get_object_or_404(User, username=username)
            if usuario:
                user = authenticate(username=username, password=password)
                if user:
                    login(request, user)
                    messages.success(request, '¡Inicio de sesion exitoso!')
                else:
                    if usuario.intentos > 2:
                        usuario.is_active = False
                        messages.error(request, 'Usuario bloqueado por demasiados intentos fallidos')
                        body = 'El usuario:'+usuario.username+ ' a intentado iniciar sesion demasiadas veces, por favor desbloqueelo'
                        res = send_email_for_enable(request,'Peticion de desbloqueo', body)
                        if res:
                            messages.success(request,'Solicitud enviada para pedir desbloqueo')
                        else:
                            messages.error(request,'No se pudo enviar peticion, contacte al administrador')
                    else: 
                        messages.error(request, 'Intento de inicio de session fallido')
                    usuario.intentos = usuario.intentos + 1
                    usuario.save()
            else: 
                messages.error(request, 'Usuario no existe')
        else:
            messages.error(request, 'Digite correctamente el nombre del usuario y contraseña')
    return redirect('/')



