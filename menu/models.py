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

            menu_items = MenuItem.objects.all()
            children = menu_items.filter(parent__name=self.name)

            if children and children[0].menu.name != self.menu.name:
                raise ValidationError(
                    f'"{self.name}" не может быть подпунктом меню "{self.menu}", '
                    f'так как подпункты текущего пункта относятся к меню "{children[0].menu.name}".'
                )

            def validate(child, parent):
                parent = parent.parent

                if parent:
                    if parent.name == self.name:
                        raise ValidationError(f'"{self.name}" не может быть подпунктом "{self.parent}"!')
                    elif parent not in children:
                        validate(child, parent)
                    elif parent in children:
                        raise ValidationError(f'"{self.name}" не может быть подпунктом "{self.parent}"!')

            validate(self.name, self.parent)

    class Meta:
        ordering = ['id']
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'
