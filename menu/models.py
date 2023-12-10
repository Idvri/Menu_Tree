from django.core.exceptions import ValidationError
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


class MenuItem(models.Model):
    name = models.CharField('Название', max_length=50, unique=True)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, verbose_name='Основное меню')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='пункт/подменю', null=True, blank=True)

    def __str__(self):
        return self.name

    def clean(self):
        if Menu.objects.filter(name=self.name).exists():
            raise ValidationError(
                'Имя пункта меню также должно быть уникальным по отношению к элементам основного меню.'
            )
        if self.parent.menu != self.menu:
            raise ValidationError(
                f'В качестве подменю может быть только тот пункт/подменю, '
                f'основным меню которого является "{self.menu}"!'
            )

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['id']
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'


