# Generated by Django 3.2 on 2023-10-19 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='libro',
            old_name='id',
            new_name='ID',
        ),
        migrations.RenameField(
            model_name='libro',
            old_name='titulo',
            new_name='Titulo',
        ),
    ]
