from django.db import models
from django.contrib.auth.models import User

class PrestacaoServicos(models.Model):
    BAIRROS_CHOICES = [
        ('', 'Selecione o bairro'),
        ('aberta_dos_morros', 'Aberta dos Morros'),
        ('agronomia', 'Agronomia'),
        ('anchieta', 'Anchieta'),
        ('arquipelago', 'Arquipélago'),
        ('auxiliadora', 'Auxiliadora'),
        ('azenha', 'Azenha'),
        ('bela_vista', 'Bela Vista'),
        ('belem_novo', 'Belém Novo'),
        ('belem_velho', 'Belém Velho'),
        ('boa_vista', 'Boa Vista'),
        ('boa_vista_do_sul', 'Boa Vista do Sul'),
        ('bom_fim', 'Bom Fim'),
        ('bom_jesus', 'Bom Jesus'),
        ('camaqua', 'Camaquã'),
        ('campo_novo', 'Campo Novo'),
        ('cascata', 'Cascata'),
        ('cavalhada', 'Cavalhada'),
        ('centro_historico', 'Centro Histórico'),
        ('chacara_das_pedras', 'Chácara das Pedras'),
        ('chapeu_do_sol', 'Chapéu do Sol'),
        ('cidade_baixa', 'Cidade Baixa'),
        ('coronel_aparicio_borges', 'Coronel Aparício Borges'),
        ('costa_e_silva', 'Costa e Silva'),
        ('cristal', 'Cristal'),
        ('cristo_redentor', 'Cristo Redentor'),
        ('espirito_santo', 'Espírito Santo'),
        ('extrema', 'Extrema'),
        ('farrapos', 'Farrapos'),
        ('farroupilha', 'Farroupilha'),
        ('floresta', 'Floresta'),
        ('gloria', 'Glória'),
        ('guaruja', 'Guarujá'),
        ('higienopolis', 'Higienópolis'),
        ('hipica', 'Hípica'),
        ('humaita', 'Humaitá'),
        ('independencia', 'Independência'),
        ('ipanema', 'Ipanema'),
        ('jardim_botanico', 'Jardim Botânico'),
        ('jardim_carvalho', 'Jardim Carvalho'),
        ('jardim_do_salso', 'Jardim do Salso'),
        ('jardim_europa', 'Jardim Europa'),
        ('jardim_floresta', 'Jardim Floresta'),
        ('jardim_isabel', 'Jardim Isabel'),
        ('jardim_itu', 'Jardim Itu'),
        ('jardim_itu_sabara', 'Jardim Itu Sabará'),
        ('jardim_leopoldina', 'Jardim Leopoldina'),
        ('jardim_lindoia', 'Jardim Lindóia'),
        ('jardim_sabara', 'Jardim Sabará'),
        ('jardim_sao_pedro', 'Jardim São Pedro'),
        ('lageado', 'Lageado'),
        ('lami', 'Lami'),
        ('lomba_do_pinheiro', 'Lomba do Pinheiro'),
        ('mario_quintana', 'Mário Quintana'),
        ('medianeira', 'Medianeira'),
        ('menino_deus', 'Menino Deus'),
        ('moinhos_de_vento', 'Moinhos de Vento'),
        ('mont_serrat', 'Mont Serrat'),
        ('morro_santana', 'Morro Santana'),
        ('navegantes', 'Navegantes'),
        ('nonoai', 'Nonoai'),
        ('parque_santa_fe', 'Parque Santa Fé'),
        ('partenon', 'Partenon'),
        ('passo_da_areia', 'Passo da Areia'),
        ('passo_das_pedras', 'Passo das Pedras'),
        ('pedra_redonda', 'Pedra Redonda'),
        ('petropolis', 'Petrópolis'),
        ('pitinga', 'Pitinga'),
        ('ponta_grossa', 'Ponta Grossa'),
        ('praia_de_belas', 'Praia de Belas'),
        ('protasio_alves', 'Protásio Alves'),
        ('restinga', 'Restinga'),
        ('rio_branco', 'Rio Branco'),
        ('rubem_berta', 'Rubem Berta'),
        ('santa_cecilia', 'Santa Cecília'),
        ('santa_maria_goretti', 'Santa Maria Goretti'),
        ('santa_rosa_de_lima', 'Santa Rosa de Lima'),
        ('santa_teresa', 'Santa Tereza'),
        ('santana', 'Santana'),
        ('santo_antonio', 'Santo Antônio'),
        ('sao_caetano', 'São Caetano'),
        ('sao_geraldo', 'São Geraldo'),
        ('sao_joao', 'São João'),
        ('sao_jose', 'São José'),
        ('sao_sebastiao', 'São Sebastião'),
        ('sarandi', 'Sarandi'),
        ('serraria', 'Serraria'),
        ('setimo_ceu', 'Sétimo Céu'),
        ('teresopolis', 'Teresópolis'),
        ('tres_figueiras', 'Três Figueiras'),
        ('tristeza', 'Tristeza'),
        ('vila_assuncao', 'Vila Assunção'),
        ('vila_conceicao', 'Vila Conceição'),
        ('vila_ipiranga', 'Vila Ipiranga'),
        ('vila_jardim', 'Vila Jardim'),
        ('vila_joao_pessoa', 'Vila João Pessoa'),
        ('vila_nova', 'Vila Nova'),
        ('vila_sao_jose', 'Vila São José')
    ]
    passeador = models.ForeignKey(User, on_delete=models.CASCADE,  unique=True)
    bairro = models.CharField(choices=BAIRROS_CHOICES, null=True, blank=True)
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