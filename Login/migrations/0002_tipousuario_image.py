# Generated by Django 4.2.6 on 2023-10-15 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tipousuario',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='imagens_perfil'),
        ),
    ]
