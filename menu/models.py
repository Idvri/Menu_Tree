from django.db import models


# Create your models here.
class Menu(models.Model):
    name = models.CharField('Название', max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'


class Item(models.Model):
    name = models.CharField('Название', max_length=50, unique=True)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='menu_items')
    item_parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'


