# Generated by Django 4.2.6 on 2023-11-25 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Serviço', '0016_selecionarhorario_complemento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='selecionarhorario',
            name='numero',
            field=models.IntegerField(default=1),
        ),
    ]
