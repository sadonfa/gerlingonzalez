# Generated by Django 5.1 on 2024-09-13 21:09

import django.db.models.deletion
import django.utils.timezone
import django_ckeditor_5.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creado el')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Actualizado el')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Titulo')),
                ('description', django_ckeditor_5.fields.CKEditor5Field(verbose_name='Descripcion')),
                ('image', models.ImageField(default='null', upload_to='blog')),
                ('published', models.BooleanField(default=False, verbose_name='Publicado')),
                ('published_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha de publicacion')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creado el')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Actualizado el')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Autor')),
                ('categories', models.ManyToManyField(related_name='get_posts', to='blog.category', verbose_name='Categorias')),
            ],
            options={
                'verbose_name': 'Entrada',
                'verbose_name_plural': 'Entradas',
                'ordering': ['-published'],
            },
        ),
    ]
