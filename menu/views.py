from django.shortcuts import render

from menu.models import Menu


# Create your views here.
def get_menus(request):
    """Эндпойнт для выбора меню."""
    return render(request, 'menu/index.html', {'menus': Menu.objects.all()})


def get_items(request, path):
    """Эндпойнт, который задействует template tag и выдаёт выбранное меню, с учётом его пунктов и подпунктов."""
    path = path.split('/')
    return render(request, 'menu/index.html', {'menu_name': path[0], 'item_name': path[-1]})
