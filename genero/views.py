from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404,render,redirect
from django.contrib import messages
from django.core.paginator import Paginator
#imports del modelo
from .models import Genero
from .forms import GeneroForm

# Create your views here.
def index_genero(request):
    genero_list = Genero.objects.all().order_by('nombre')
    paginator = Paginator(genero_list, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'genero/index.html', {'page_obj': page_obj})

def create_genero(request):
    return render(request, 'genero/create.html')

def edit_genero(request, genero_id):
    genero = get_object_or_404(Genero,pk=genero_id)
    return render(request, 'genero/edit.html', {'genero': genero})

def update_genero(request, genero_id):
    genero =  get_object_or_404(Genero, pk=genero_id)
    if request.method == 'POST':
        form = GeneroForm(request.POST, instance=genero)
        form.save()
        messages.success(request, 'Genero actualizado correctamente')
    return redirect('/genero')

def store_genero(request):
    if request.method == 'POST':
        form = GeneroForm(request.POST)
        if form.is_valid():
            form.save()
 
            messages.success(request, 'Profesión Guardada correctamente')
        else:
            errors=form.errors
            return render(request, 'genero/create.html',{'errors': errors})
    return redirect('/genero')

    