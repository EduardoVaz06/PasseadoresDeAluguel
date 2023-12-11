from django.db import models
from django.contrib.auth.models import User
from Serviço.models import SelecionarHorario

class Avaliacao(models.Model):
    passeador = models.ForeignKey(User, on_delete=models.CASCADE)
    passeio = models.ForeignKey(SelecionarHorario, on_delete=models.CASCADE)
    pontuacao = models.IntegerField()