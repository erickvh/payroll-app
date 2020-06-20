from usuario.models import Menu
from usuario.models import User
from django.core import serializers
from django.contrib.auth.models import Group

def FilterMenu(get_response):

    def middleware(request):
        if request.user.username:
            user = User.objects.filter(username=request.user.username).first()
            groups = user.groups.all()
            lista =  dict()
            for group in groups:
                menu = group.menu_set.filter(padre=None)
                for me in menu:
                    for m in Menu.objects.filter(padre=me):
                        lista[me.nombre] = {m.nombre:m.url}
            request.session['lista'] = lista
        response = get_response(request)
        print(request.session['lista'])
        return response
    return middleware