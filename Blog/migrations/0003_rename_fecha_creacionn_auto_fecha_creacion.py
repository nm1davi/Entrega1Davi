# Generated by Django 4.0.6 on 2022-07-05 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_rename_nombre_auto_marca_rename_edad_auto_modelo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='auto',
            old_name='fecha_creacion',
            new_name='fecha_creacion',
        ),
    ]
