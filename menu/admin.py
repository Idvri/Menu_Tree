from django.contrib import admin

from menu.models import Menu, Item


# Register your models here.
@admin.register(Menu)
class Menu(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Item)
class Item(admin.ModelAdmin):
    list_display = ('name', 'menu', 'item_parent')
