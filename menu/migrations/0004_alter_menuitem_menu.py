# Generated by Django 5.0 on 2023-12-10 15:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_rename_item_menuitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.menu'),
        ),
    ]
