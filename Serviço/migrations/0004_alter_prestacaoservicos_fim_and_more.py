# Generated by Django 4.2.6 on 2023-11-15 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Serviço', '0003_prestacaoservicos_fim_prestacaoservicos_inicio_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestacaoservicos',
            name='fim',
            field=models.TimeField(default='19:00'),
        ),
        migrations.AlterField(
            model_name='prestacaoservicos',
            name='inicio',
            field=models.TimeField(default='06:00'),
        ),
    ]
