from django.shortcuts import render

from menu.models import Menu


# Create your views here.
def get_menus(request):
    return render(request, 'menu/index.html', {'menus': Menu.objects.all()})


def get_items(request, path):
    path = path.split('/')
    return render(request, 'menu/index.html', {'menu_name': path[0], 'item_name': path[-1]})
