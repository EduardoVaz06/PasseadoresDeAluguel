# Generated by Django 4.2.6 on 2023-11-25 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Serviço', '0020_selecionarhorario_complemento_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='selecionarhorario',
            name='complemento',
        ),
        migrations.RemoveField(
            model_name='selecionarhorario',
            name='extras',
        ),
        migrations.RemoveField(
            model_name='selecionarhorario',
            name='numero',
        ),
        migrations.RemoveField(
            model_name='selecionarhorario',
            name='rua',
        ),
    ]
