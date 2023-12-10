from django.urls import path

from menu.apps import MenuConfig
from menu.views import get_menus, get_items

app_name = MenuConfig.name

urlpatterns = [
    path('', get_menus, name='main_menu'),
    path('<path:path>/', get_items, name='menu_items'),
]
