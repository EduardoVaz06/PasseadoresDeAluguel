
from django.shortcuts import render, redirect
from Serviço.models import PrestacaoServicos, SelecionarHorario
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from Avaliação.models import Avaliacao

@login_required
def agenda_passeador(request, user_id):
    user_to_view = get_object_or_404(User, id=user_id)

    # Recupera os dados da tabela PrestacaoServicos para o passeador específico
    prestacao_servicos = PrestacaoServicos.objects.filter(passeador=user_to_view)

    # Filtra os horários selecionados com base no passeador específico
    horarios_selecionados = SelecionarHorario.objects.filter(id_passeador__in=prestacao_servicos)

    # Adiciona os nomes dos usuários solicitantes ao contexto
    detalhes_horarios = []
    for horario in horarios_selecionados:
        nome_solicitante = f"{horario.id_usuario.first_name} {horario.id_usuario.last_name}"
        detalhes_horarios.append({'horario': horario.horario, 'status': horario.status, 'nome_solicitante': nome_solicitante, 'id_solicitacao': horario.id})

    context = {'detalhes_horarios': detalhes_horarios}
    return render(request, 'agenda/agenda_passeador.html', context)

def atualizar_status(request, horario_id):
    if request.method == 'POST':
        novo_status = request.POST.get('novo_status')
        # Atualize o status do horário com base no valor de novo_status
        # Certifique-se de verificar se o usuário tem permissão para fazer essa atualização
    return redirect('agenda_passeador')

def aceitar_passeio(request, horario_id):
    # Lógica para encontrar e atualizar o status para "aceito"
    horario = get_object_or_404(SelecionarHorario, id=horario_id)
    horario.status = "Aceito"
    horario.save()
    return redirect('agenda_passeador', user_id=request.user.id )  # Substitua com a URL correta da sua agenda

def recusar_passeio(request, horario_id):
    # Lógica para encontrar e atualizar o status para "recusado"
    horario = get_object_or_404(SelecionarHorario, id=horario_id)
    horario.status = "Recusado"
    horario.save()
    return redirect('agenda_passeador', user_id=request.user.id )  # Substitua com a URL correta da sua agenda

def finalizar_passeio(request, horario_id):
    # Lógica para encontrar e atualizar o status para "recusado"
    horario = get_object_or_404(SelecionarHorario, id=horario_id)
    horario.status = "Finalizado"
    horario.save()
    return redirect('agenda_passeador', user_id=request.user.id )  # Substitua com a URL correta da sua agenda

def passeios_finalizados(request, user_id):
    user_to_view = get_object_or_404(User, id=user_id)

    # Recupera os dados da tabela PrestacaoServicos para o passeador específico
    prestacao_servicos = PrestacaoServicos.objects.filter(passeador=user_to_view)

    # Filtra os horários selecionados com base no passeador específico
    horarios_selecionados = SelecionarHorario.objects.filter(id_passeador__in=prestacao_servicos)

    # Adiciona os nomes dos usuários solicitantes ao contexto
    detalhes_horarios = []
    for horario in horarios_selecionados:
        nome_solicitante = f"{horario.id_usuario.first_name} {horario.id_usuario.last_name}"
        detalhes_horarios.append({'horario': horario.horario, 'status': horario.status, 'nome_solicitante': nome_solicitante, 'id_solicitacao': horario.id})

    context = {'detalhes_horarios': detalhes_horarios}
    return render(request, 'agenda/passeios_finalizados.html', context)

def passeios_solicitados(request, user_id):
    user_to_view = get_object_or_404(User, id=user_id)

    # Recupera os dados da tabela PrestacaoServicos para o passeador específico
    prestacao_servicos = PrestacaoServicos.objects.filter(passeador=user_to_view)

    # Filtra os horários selecionados com base no passeador específico
    horarios_selecionados = SelecionarHorario.objects.filter(id_passeador__in=prestacao_servicos)

    # Adiciona os nomes dos usuários solicitantes ao contexto
    detalhes_horarios = []
    for horario in horarios_selecionados:
        nome_solicitante = f"{horario.id_usuario.first_name} {horario.id_usuario.last_name}"
        detalhes_horarios.append({'horario': horario.horario, 'status': horario.status, 'nome_solicitante': nome_solicitante, 'id_solicitacao': horario.id})

    context = {'detalhes_horarios': detalhes_horarios}
    return render(request, 'agenda/passeios_solicitados.html', context)

def agenda_usuario(request, user_id):
    user_to_view = get_object_or_404(User, id=user_id)

    # Recupera os dados da tabela SelecionarHorario para o usuário específico
    horarios_selecionados = SelecionarHorario.objects.filter(id_usuario=user_to_view)

    # Adiciona os nomes dos passeadores ao contexto
    detalhes_horarios = []
    for horario in horarios_selecionados:
        nome_passeador = f"{horario.id_passeador.passeador.first_name} {horario.id_passeador.passeador.last_name}"
        detalhes_horarios.append({'horario': horario.horario, 'status': horario.status, 'nome_passeador': nome_passeador, 'id_solicitacao': horario.id})

    context = {'detalhes_horarios': detalhes_horarios}
    return render(request, 'agenda/agenda_usuario.html', context)

def passeios_finalizados_user(request, user_id):
    user_to_view = get_object_or_404(User, id=user_id)

    # Recupera os dados da tabela SelecionarHorario para o usuário específico
    horarios_selecionados = SelecionarHorario.objects.filter(id_usuario=user_to_view)

    # Adiciona os nomes dos passeadores ao contexto
    detalhes_horarios = []
    for horario in horarios_selecionados:
        nome_passeador = f"{horario.id_passeador.passeador.first_name} {horario.id_passeador.passeador.last_name}"
        
        # Verifica se existe uma avaliação para o passeio
        try:
            avaliacao = Avaliacao.objects.get(passeio=horario)
            pontuacao = avaliacao.pontuacao
        except Avaliacao.DoesNotExist:
            pontuacao = None

        detalhes_horarios.append({
            'horario': horario.horario,
            'status': horario.status,
            'nome_passeador': nome_passeador,
            'id_solicitacao': horario.id,
            'pontuacao': pontuacao,
        })

    context = {'detalhes_horarios': detalhes_horarios}
    return render(request, 'agenda/passeios_finalizados_user.html', context)

def passeios_solicitados_user(request, user_id):
    user_to_view = get_object_or_404(User, id=user_id)

    # Recupera os dados da tabela SelecionarHorario para o usuário específico
    horarios_selecionados = SelecionarHorario.objects.filter(id_usuario=user_to_view)

    # Adiciona os nomes dos passeadores ao contexto
    detalhes_horarios = []
    for horario in horarios_selecionados:
        nome_passeador = f"{horario.id_passeador.passeador.first_name} {horario.id_passeador.passeador.last_name}"
        detalhes_horarios.append({'horario': horario.horario, 'status': horario.status, 'nome_passeador': nome_passeador, 'id_solicitacao': horario.id})

    context = {'detalhes_horarios': detalhes_horarios}
    return render(request, 'agenda/passeios_solicitados_user.html', context)