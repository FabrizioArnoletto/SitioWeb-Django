# Generated by Django 3.2 on 2023-11-09 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0003_libro_fecha'),
    ]

    operations = [
        migrations.CreateModel(
            name='comentarios',
            fields=[
                ('ID_c', models.AutoField(primary_key=True, serialize=False)),
                ('Comentario', models.TextField(null=True, verbose_name='Comentario')),
                ('ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libreria.libro')),
            ],
        ),
    ]
