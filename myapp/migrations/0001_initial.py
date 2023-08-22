# Generated by Django 4.2.4 on 2023-08-22 21:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Biblioteca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Ingrese el nombre de la Biblioteca', max_length=50)),
                ('ubicacion', models.CharField(help_text='Ingrese la ubicacion de la Biblioteca', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(help_text='Ingrese el titulo del Libro', max_length=50)),
                ('ISBN', models.CharField(help_text='Ingrese el ISBN del Libro', max_length=13)),
                ('autor', models.CharField(help_text='Ingrese el nombre del autor', max_length=50)),
                ('estado', models.CharField(help_text='Ingrese el estado del Libro', max_length=8)),
                ('bibliotecas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.biblioteca')),
            ],
        ),
    ]
