from django.core.exceptions import ValidationError
from django.db import models


# Create your models here.
class Menu(models.Model):
    name = models.CharField('Название', max_length=50, unique=True)

    def __str__(self):
        return self.name

    def clean(self):
        if MenuItem.objects.filter(name=self.name).exists():
            raise ValidationError(
                'Название основного меню также должно быть уникальным по отношению к названиям пунктов/подменю.'
            )

    class Meta:
        ordering = ['id']
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'


class MenuItem(models.Model):
    name = models.CharField('Название', max_length=50, unique=True)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, verbose_name='Основное меню')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='пункт/подменю', null=True, blank=True)

    def __str__(self):
        return self.name

    def clean(self):
        if Menu.objects.filter(name=self.name).exists():
            raise ValidationError(
                'Название пункта меню также должно быть уникальным по отношению к названиям элементов основного меню.'
            )
        elif self.parent:
            if self.parent.menu != self.menu:
                raise ValidationError(
                    f'В качестве подменю может быть только тот пункт/подменю, '
                    f'основным меню которого является "{self.menu}"!'
                )
            elif self.parent.name == self.name:
                raise ValidationError(
                    'Пункт не может быть своим же пунктом/подменю!'
                )

            children = list(MenuItem.objects.filter(parent__name=self.name))
            parent = self.parent.parent

            if parent in children:
                raise ValidationError(
                    f'{self.name} не может быть подпунктом {parent.name}!'
                )
            if parent and self.name == parent.name:
                raise ValidationError(
                    f'{self.name} не может быть подпунктом {self.parent}!'
                )

    class Meta:
        ordering = ['id']
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'
