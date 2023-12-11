from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegistrarForm
from django.contrib import messages
from .models import TipoUsuario  # Importe o modelo TipoUsuario
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import TipoUsuario
from Serviço.forms import PrestacaoServicosForm
from .forms import PesquisaServicoForm
from Serviço.models import PrestacaoServicos, SelecionarHorario
from datetime import datetime, timedelta
from Serviço.models import InfoPasseio
from django.db.models import Avg
from Avaliação.models import Avaliacao

# Create your views here.
def logar(request):
    if request.user.is_authenticated:
        tipo_usuario = TipoUsuario.objects.get(user=request.user).tipo

        if tipo_usuario == 'usuario':
            return redirect('home_usuario')
        elif tipo_usuario == 'passeador':
            return redirect('home_passeador')
        else:
            messages.error(request, "Tipo de usuário desconhecido.")
            return redirect('login')

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            tipo_usuario = TipoUsuario.objects.get(user=user).tipo

            if tipo_usuario == 'usuario':
                return redirect('home_usuario')
            elif tipo_usuario == 'passeador':
                return redirect('home_passeador')
            else:
                messages.error(request, "Tipo de usuário desconhecido.")
                return redirect('login')
        else:
            messages.info(request, "Usuário ou senha incorretos")

    context = {}
    return render(request, 'login/login.html', context)

def deslogar(request):
    logout(request)
    return redirect('login')

def registrar(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = RegistrarForm()

        if request.method == "POST":
            form = RegistrarForm(request.POST)
            if form.is_valid():
                user = form.save()
                tipo_usuario = form.cleaned_data['tipo_usuario']
                telefone = form.cleaned_data['telefone']
                # Crie um novo objeto TipoUsuario associado ao usuário
                TipoUsuario.objects.create(user=user, tipo=tipo_usuario, telefone=telefone)

                messages.success(request, 'conta criada com sucesso, ' + user.username)
                return redirect('login')

        context = {'form': form}
        return render(request, 'login/registrar.html', context)
    
def home_usuario(request):
    pesquisa_form = PesquisaServicoForm(request.GET)

    servicos = PrestacaoServicos.objects.all()
    pesquisa_clicada = False

    if pesquisa_form.is_valid():
        pesquisa_clicada = request.GET.get('pesquisa_clicada')
        bairro = pesquisa_form.cleaned_data.get('bairro')
        duracao_passeio = pesquisa_form.cleaned_data.get('duracao_passeio')

        if bairro:
            servicos = servicos.filter(bairro__icontains=bairro)
        if duracao_passeio:
            servicos = servicos.filter(duracao_passeio=duracao_passeio)

        # Busca a média de avaliação para cada passeador
        media_avaliacoes = Avaliacao.objects.values('passeador').annotate(media=Avg('pontuacao'))

        # Converte a média para um dicionário, onde a chave é o ID do passeador
        media_dict = {item['passeador']: item['media'] for item in media_avaliacoes}

        passeadores_info = [
            {
                'passeador_id': servico.passeador.id,
                'nome_passeador': f"{servico.passeador.first_name} {servico.passeador.last_name}",
                'duracao_passeio': servico.duracao_passeio,
                'inicio': servico.inicio,
                'fim': servico.fim,
            }
            for servico in servicos
        ]

        # Adiciona a média de avaliação ao dicionário para cada passeador
        for passeador_info in passeadores_info:
            passeador_info['media_avaliacao'] = media_dict.get(passeador_info['passeador_id'], 0)

        # Filtra passeadores com avaliação nula e ordena pela média de avaliação em ordem decrescente
        passeadores_info = sorted([p for p in passeadores_info if p['media_avaliacao'] is not None], key=lambda x: x['media_avaliacao'], reverse=True)

    tipo_usuario = TipoUsuario.objects.get(user=request.user)
    if tipo_usuario.tipo == 'passeador':
        return redirect('home_passeador')

    return render(request, 'home/home_usuario.html', {'pesquisa_form': pesquisa_form, 'passeadores_info': passeadores_info, 'pesquisa_clicada': pesquisa_clicada})

@login_required(login_url='login')
def home_passeador(request):
    tipo_usuario = TipoUsuario.objects.get(user=request.user)

    if tipo_usuario.tipo == 'passeador':
        user = request.user
        prestacao_servico, created = PrestacaoServicos.objects.get_or_create(passeador=user)

        if request.method == 'POST':
            form = PrestacaoServicosForm(request.POST, instance=prestacao_servico)
            if form.is_valid():
                form.save()
        else:
            form = PrestacaoServicosForm(instance=prestacao_servico)

        return render(request, 'home/home_passeador.html', {'form': form})
    else:
        return redirect('login')

def index(request):
    return render(request, 'includes/index.html')

def infos(request):
    return render(request, 'includes/infos.html')

def duracao_para_timedelta(duracao):
    if duracao.endswith('h'):
        return timedelta(hours=int(duracao[:-1]))
    elif duracao.endswith('m'):
        return timedelta(minutes=int(duracao[:-1]))
    else:
        return timedelta()

def gerar_opcoes_horario(prestacao_servicos):
    opcoes_horario = []

    for servico in prestacao_servicos:
        hora_inicio = datetime.strptime(str(servico.inicio), '%H:%M:%S')
        hora_fim = datetime.strptime(str(servico.fim), '%H:%M:%S')
        duracao_passeio = duracao_para_timedelta(servico.duracao_passeio)

        while hora_inicio + duracao_passeio <= hora_fim:
            opcao = {
                'inicio': hora_inicio.strftime('%H:%M'),
                'fim': (hora_inicio + duracao_passeio).strftime('%H:%M')
            }
            opcoes_horario.append(opcao)
            hora_inicio += duracao_passeio

    return opcoes_horario

def horarios_view(request, passeador_id):
    # Recupera os dados da tabela PrestacaoServicos para o passeador específico
    prestacao_servicos = PrestacaoServicos.objects.filter(passeador_id=passeador_id)

    # Gera as opções de horário com base nos dados da tabela
    opcoes_horario = gerar_opcoes_horario(prestacao_servicos)

    return render(request, 'includes/horarios.html', {'opcoes_horario': opcoes_horario})


def selecionar_horario(request):
    if request.method == 'POST':
        # Obter o ID do passeador a partir do contexto da página
        id_passeador = request.POST.get('id_passeador')

        # Consultar o objeto PrestacaoServicos com base no ID
        passeador_instance = get_object_or_404(PrestacaoServicos, passeador_id=id_passeador)

        # Criar uma instância de SelecaoHorario e salvar no banco de dados
        selecao = SelecionarHorario(id_usuario=request.user, id_passeador=passeador_instance, horario=request.POST['horario_selecionado'])
        selecao.save()

        # Salvar informações adicionais no modelo InfoPasseio
        info_passeio = InfoPasseio(
            id_passeio=selecao,
            rua=request.POST['rua'],
            numero=request.POST['numero'],
            complemento=request.POST['complemento'],
            extras=request.POST['extras']
        )
        info_passeio.save()

        messages.success(request, 'Passeio agendado com sucesso!')
        return redirect('home_usuario')
    
    return render(request, 'includes/horarios.html')

def info_passeio(request, id_passeio_id):
    info_passeio = get_object_or_404(InfoPasseio, id_passeio_id=id_passeio_id)
    return render(request, 'solicitacao/info_passeio.html', {'info_passeio': info_passeio})

def teste_view(request):
    return render(request, 'includes/guardar.html')
