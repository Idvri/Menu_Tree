from django import template
from django.core.exceptions import ObjectDoesNotExist

from menu.models import Item

register = template.Library()


@register.inclusion_tag('menu/items.html')
def get_submenu(menu_name, item_name):
    items = Item.objects.filter(menu__name=menu_name)

    def get_menu(first_menu: str = None, second_menu: list = None):

        if first_menu is None:
            menu = list(items.filter(item_parent__name=None))
        else:
            menu = list(items.filter(item_parent__name=first_menu))

        try:
            print(menu.index(second_menu[0].item_parent))
            menu.insert(menu.index(second_menu[0].item_parent) + 1, second_menu)
        except (IndexError, TypeError):
            pass

        try:
            return get_menu(items.get(name=first_menu).item_parent.name, menu)
        except AttributeError:
            return get_menu(second_menu=menu)
        except ObjectDoesNotExist:
            return menu

    if menu_name == item_name:
        return {'items': get_menu()}
    else:
        return {'items': get_menu(item_name)}
