from django.shortcuts import render, get_object_or_404
from .models import Perfil
from Login.models import TipoUsuario
from Serviço.models import PrestacaoServicos
from Login.views import gerar_opcoes_horario
from django.contrib.auth.decorators import login_required
from django.contrib import messages  # Importe messages para mostrar mensagens de sucesso ou erro
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import CustomUserChangeForm 
from django.contrib.auth import update_session_auth_hash
from .forms import UserProfileForm
from django.db.models import Avg
from Avaliação.models import Avaliacao
from django.urls import reverse

@login_required
def visualizar_perfil(request):
    perfil = Perfil.objects.get(user=request.user)
    tipo_usuario = TipoUsuario.objects.get(user=request.user)
    context = {'perfil': perfil, 'tipo_usuario': tipo_usuario}
    return render(request, 'perfil/perfil.html', context)

@login_required
def editar_perfil(request):
    perfil = Perfil.objects.get(user=request.user)
    tipo_usuario = TipoUsuario.objects.get(user=request.user)

    if request.method == "POST":
        user_form = CustomUserChangeForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=tipo_usuario)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Seu perfil foi atualizado com sucesso!')
            return redirect('perfil')
    else:
        user_form = CustomUserChangeForm(instance=request.user)
        profile_form = UserProfileForm(instance=tipo_usuario)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }
    return render(request, 'perfil/editar_perfil.html', context)

@login_required
def editar_perfil_passeador(request):
    perfil = Perfil.objects.get(user=request.user)
    tipo_usuario = TipoUsuario.objects.get(user=request.user)

    if request.method == "POST":
        user_form = CustomUserChangeForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=tipo_usuario)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Seu perfil foi atualizado com sucesso!')
            return redirect(reverse('perfil_passeador_self', args=[request.user.id]))
    else:
        user_form = CustomUserChangeForm(instance=request.user)
        profile_form = UserProfileForm(instance=tipo_usuario)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }
    return render(request, 'perfil/editar_perfil_passeador.html', context)


@login_required
def perfil_passeador(request, user_id):
    user_to_view = get_object_or_404(User, id=user_id)
    perfil_to_view = get_object_or_404(Perfil, user=user_to_view)
    tipo_usuario = TipoUsuario.objects.get(user=user_to_view)

    # Recupera os dados da tabela PrestacaoServicos para o passeador específico
    prestacao_servicos = PrestacaoServicos.objects.filter(passeador=user_to_view)

    # Gera as opções de horário com base nos dados da tabela
    opcoes_horario = gerar_opcoes_horario(prestacao_servicos)

    # Calcula a média das avaliações do passeador
    media_avaliacoes = Avaliacao.objects.filter(passeador=user_to_view).aggregate(media=Avg('pontuacao'))['media']

    context = {'perfil': perfil_to_view, 'tipo_usuario': tipo_usuario, 'opcoes_horario': opcoes_horario, 'media_avaliacoes': media_avaliacoes}
    return render(request, 'perfil/perfil_passeador.html', context)

@login_required
def perfil_passeador_self(request, user_id):
    user_to_view = get_object_or_404(User, id=user_id)
    perfil_to_view = get_object_or_404(Perfil, user=user_to_view)
    tipo_usuario = TipoUsuario.objects.get(user=user_to_view)

    # Recupera os dados da tabela PrestacaoServicos para o passeador específico
    prestacao_servicos = PrestacaoServicos.objects.filter(passeador=user_to_view)

    # Gera as opções de horário com base nos dados da tabela
    opcoes_horario = gerar_opcoes_horario(prestacao_servicos)

    # Calcula a média das avaliações do passeador
    media_avaliacoes = Avaliacao.objects.filter(passeador=user_to_view).aggregate(media=Avg('pontuacao'))['media']

    context = {'perfil': perfil_to_view, 'tipo_usuario': tipo_usuario, 'opcoes_horario': opcoes_horario, 'media_avaliacoes': media_avaliacoes}
    return render(request, 'perfil/perfil_passeador_self.html', context)
