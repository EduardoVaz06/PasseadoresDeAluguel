# Generated by Django 4.2.6 on 2023-11-15 22:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Serviço', '0004_alter_prestacaoservicos_fim_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SelecaoHorario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horario', models.CharField(max_length=20)),
                ('status', models.CharField(choices=[('solicitado', 'Solicitado'), ('aceito', 'Aceito'), ('concluido', 'Concluído')], default='solicitado', max_length=20)),
                ('id_passeador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='selecao_horario_passeador', to=settings.AUTH_USER_MODEL)),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='selecao_horario_usuario', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
