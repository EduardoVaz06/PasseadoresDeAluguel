# Generated by Django 4.2.6 on 2023-11-25 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Serviço', '0014_alter_selecionarhorario_id_delete_selecaodehorario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='selecionarhorario',
            name='status',
            field=models.CharField(default='Solicitado', max_length=20),
        ),
        migrations.CreateModel(
            name='InfoPasseio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rua', models.CharField(max_length=100)),
                ('numero', models.IntegerField()),
                ('complemento', models.CharField(blank=True, max_length=100, null=True)),
                ('extras', models.TextField(blank=True, null=True)),
                ('id_passeio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Serviço.selecionarhorario')),
            ],
        ),
    ]
