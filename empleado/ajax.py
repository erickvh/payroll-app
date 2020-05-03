from django.http import JsonResponse

from municipio.models import Municipio
from departamento.models import Departamento


def get_municipios(request):
    departamento_id = request.GET.get('departamento_id')
    municipios = Municipio.objects.none()
    options = '<option value="" selected="selected">Seleccione un municipio</option>'
    if departamento_id:
        municipios = Municipio.objects.filter(departamento_id=departamento_id)   
    for municipio in municipios:
        options += '<option value="%s">%s</option>' % (
            municipio.id,
            municipio.nombre
        )
    response = {}
    response['municipios'] = options
    return JsonResponse(response)


