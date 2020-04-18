from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404,render,redirect
from django.contrib import messages
from django.core.paginator import Paginator
#imports del modelo
from .models import Profesion
from .forms import ProfesionForm

# Create your views here.
def index_profesion(request):
    profesiones = Profesion.objects.all().order_by('nombre')
    paginator = Paginator(profesiones, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'profesion/index.html', {'page_obj': page_obj})

def create_profesion(request):
    return render(request, 'profesion/create.html')

def edit_profesion(request, profesion_id):
    profesion = get_object_or_404(Profesion,pk=profesion_id)
    return render(request, 'profesion/edit.html', {'profesion': profesion})

def update_profesion(request, profesion_id):
    profesion =  get_object_or_404(Profesion, pk=profesion_id)
    if request.method == 'POST':
        form = ProfesionForm(request.POST, instance=profesion)
        form.save()
        messages.success(request, 'Profesión actualizada correctamente')
    return redirect('/profesion')

def store_profesion(request):
    if request.method == 'POST':
        form = ProfesionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profesión Guardada correctamente')
    return redirect('/profesion')

    