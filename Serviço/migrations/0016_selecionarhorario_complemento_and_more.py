# Generated by Django 4.2.6 on 2023-11-25 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Serviço', '0015_alter_selecionarhorario_status_infopasseio'),
    ]

    operations = [
        migrations.AddField(
            model_name='selecionarhorario',
            name='complemento',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='selecionarhorario',
            name='extras',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='selecionarhorario',
            name='numero',
            field=models.IntegerField(default='1'),
        ),
        migrations.AddField(
            model_name='selecionarhorario',
            name='rua',
            field=models.CharField(default='Rua', max_length=100),
        ),
    ]
