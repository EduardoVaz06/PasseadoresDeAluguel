# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Avaliacao
from Serviço.models import SelecionarHorario
from django.contrib.auth.decorators import login_required

@login_required
def avaliar_passeador(request, id_solicitacao):
    if request.method == 'POST':
        pontuacao = request.POST.get('pontuacao')

        # Obter o passeador associado a esta solicitação
        horario_selecionado = get_object_or_404(SelecionarHorario, id=id_solicitacao)
        passeador = horario_selecionado.id_passeador.passeador

        # Criar a avaliação
        Avaliacao.objects.create(
            passeador=passeador,
            passeio=horario_selecionado,
            pontuacao=pontuacao
        )

        return redirect('passeios_finalizados_user', user_id=request.user.id)

    return redirect('home')  # Redirecionar para a home se o método não for POST