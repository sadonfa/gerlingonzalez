# Generated by Django 5.1 on 2024-09-11 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0002_knowledges_alter_certificate_verificate'),
    ]

    operations = [
        migrations.CreateModel(
            name='SkillsCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Titulo')),
                ('percentage', models.IntegerField(verbose_name='Titulo')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Creacion')),
                ('updated', models.DateField(auto_now=True, verbose_name='Actualizacion')),
            ],
            options={
                'verbose_name': 'Habilidades de Codigo',
                'verbose_name_plural': 'Habilidades de Codigos',
            },
        ),
        migrations.CreateModel(
            name='SkillsDesing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Titulo')),
                ('percentage', models.IntegerField(verbose_name='Titulo')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Creacion')),
                ('updated', models.DateField(auto_now=True, verbose_name='Actualizacion')),
            ],
            options={
                'verbose_name': 'Habilidades de Diseño',
                'verbose_name_plural': 'Habilidades de Diseños',
            },
        ),
    ]
