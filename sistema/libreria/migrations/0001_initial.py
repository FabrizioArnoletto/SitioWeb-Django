# Generated by Django 3.2 on 2023-10-19 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=100, verbose_name='Titulo')),
                ('Imagen', models.ImageField(null=True, upload_to='imagenes/', verbose_name='Imagen')),
                ('Descripcion', models.TextField(null=True, verbose_name='Descripción')),
            ],
        ),
    ]