from django.core.exceptions import ValidationError
from django.db import models


# Create your models here.
class Menu(models.Model):
    """Модель, описывающая основное меню."""
    name = models.CharField('Название', max_length=50, unique=True)

    def __str__(self):
        return self.name

    def clean(self):
        """Метод, который валидирует название меню в зависимости от существующих названий пунктов меню."""
        if MenuItem.objects.filter(name=self.name).exists():
            raise ValidationError(
                'Название основного меню также должно быть уникальным по отношению к названиям пунктов меню.'
            )

    class Meta:
        ordering = ['id']
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'


class MenuItem(models.Model):
    """Модель, описывающая основное пункты меню."""
    name = models.CharField('Название', max_length=50, unique=True)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, verbose_name='Основное меню')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='Пункт/подменю', null=True, blank=True)

    def __str__(self):
        return self.name

    def clean(self):
        """Метод, который валидирует название пункта меню в зависимости от существующих названий основных меню."""
        if Menu.objects.filter(name=self.name).exists():
            raise ValidationError(
                'Название пункта меню также должно быть уникальным по отношению к названиям основных меню.'
            )
        elif self.parent:
            if self.parent.menu != self.menu:
                raise ValidationError(
                    f'{self.name} не может быть подпунктом "{self.parent}", '
                    f'так как их основные меню отличаются!'
                )
            elif self.parent.name == self.name:
                raise ValidationError(
                    'Пункт не может быть своим же подпунктом!'
                )

            menu_items = MenuItem.objects.all()
            children = menu_items.filter(parent__name=self.name)

            if children and children[0].menu.name != self.menu.name:
                raise ValidationError(
                    f'"{self.name}" не может быть подпунктом меню "{self.menu}", '
                    f'так как подпункты текущего пункта относятся к меню "{children[0].menu.name}".'
                )

            def validate(child, parent):
                """Функция, которая проверяет возможность пункта быть подпунктом другого пункта.
                К примеру, (старший) пункт не может быть подпунктом своего же (младшего) подпункта."""
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
