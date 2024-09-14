# Generated by Django 5.1 on 2024-08-31 00:31

import django_ckeditor_5.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Titulo')),
                ('icon', models.CharField(max_length=200, verbose_name='ICON')),
                ('description', django_ckeditor_5.fields.CKEditor5Field(verbose_name='Text')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Creacion')),
                ('updated', models.DateField(auto_now=True, verbose_name='Actualizacion')),
            ],
            options={
                'verbose_name': 'Haabilidad',
                'verbose_name_plural': 'Habilidades',
            },
        ),
    ]
