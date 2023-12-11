from django.shortcuts import render, redirect
from .forms import PrestacaoServicosForm
from django.contrib.auth.decorators import login_required
from .models import PrestacaoServicos
from .forms import InfoPasseioForm

@login_required(login_url='login')
def cadastrar_prestacao_servicos(request):
    if request.method == 'POST':
        form = PrestacaoServicosForm(request.POST)
        if form.is_valid():
            prestacao_servicos = form.save(commit=False)
            prestacao_servicos.passeador = request.user  # Associe o passeador ao usuário logado
            prestacao_servicos.save()
            return redirect('home_passeador')  # Redirecione para a página inicial do passeador
    else:
        form = PrestacaoServicosForm()

    return render(request, 'cadastrar_prestacao_servicos.html', {'form': form})

def adicionar_info_passeio(request):
    if request.method == 'POST':
        form = InfoPasseioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_usuario')  # Substitua com a URL desejada após o envio do formulário
    else:
        form = InfoPasseioForm()

    return render(request, 'solicitacao/adicionar_info_passeio.html', {'form': form})