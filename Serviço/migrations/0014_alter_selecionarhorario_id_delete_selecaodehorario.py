# Generated by Django 4.2.6 on 2023-11-25 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Serviço', '0013_alter_prestacaoservicos_passeador_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='selecionarhorario',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.DeleteModel(
            name='SelecaoDeHorario',
        ),
    ]
