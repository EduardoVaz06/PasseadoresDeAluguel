from django.db import models
from django.contrib.auth.models import User

class PrestacaoServicos(models.Model):
    passeador = models.ForeignKey(User, on_delete=models.CASCADE,  unique=True)
    bairro = models.CharField(max_length=100)
    duracao_passeio = models.CharField(max_length=10, choices=[('30m', '30 minutos'), ('1h', '1 hora')])
    inicio = models.TimeField(default='06:00')
    fim = models.TimeField(default='19:00')
    
class SelecionarHorario(models.Model):
    id = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    id_passeador = models.ForeignKey(PrestacaoServicos, to_field='passeador_id', on_delete=models.CASCADE)
    horario = models.CharField(max_length=20)
    status = models.CharField(max_length=20, default='Solicitado')

class InfoPasseio(models.Model):
    id_passeio = models.ForeignKey(SelecionarHorario, on_delete=models.CASCADE)
    rua = models.CharField(max_length=100)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=100, blank=True, null=True)
    extras = models.TextField(blank=True, null=True)