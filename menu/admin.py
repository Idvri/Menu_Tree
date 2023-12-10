from django.contrib import admin

from menu.models import Menu, MenuItem


# Register your models here.
@admin.register(Menu)
class Menu(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(MenuItem)
class Item(admin.ModelAdmin):
    list_display = ('name', 'menu', 'parent')
