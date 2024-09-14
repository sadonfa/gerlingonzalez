# Generated by Django 5.1 on 2024-09-11 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Knowledges',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Titulo')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Creacion')),
                ('updated', models.DateField(auto_now=True, verbose_name='Actualizacion')),
            ],
            options={
                'verbose_name': 'Conocimiento',
                'verbose_name_plural': 'Conocimientos',
            },
        ),
        migrations.AlterField(
            model_name='certificate',
            name='verificate',
            field=models.CharField(max_length=150, verbose_name='Id de verificacion'),
        ),
    ]
