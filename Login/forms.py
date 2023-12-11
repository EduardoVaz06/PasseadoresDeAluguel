from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import TipoUsuario

class RegistrarForm(UserCreationForm):
    tipo_usuario = forms.ChoiceField(choices=TipoUsuario.TIPOS_USUARIO, label='Tipo de Usuário')
    telefone = forms.CharField(max_length=15, label='Telefone')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'telefone', 'tipo_usuario']
        
class PesquisaForm(forms.Form):
    TIPOS_USUARIO = (
        ('', 'Escolha o tipo'),  # Opção em branco para seleção inicial
        ('usuario', 'Usuário'),
        ('passeador', 'Passeador'),
    )

    tipo_usuario = forms.ChoiceField(
        choices=TIPOS_USUARIO,
        required=False,  # Permite a escolha em branco
        label='Tipo de Usuário',
    )

    def pesquisar_usuarios(self):
        tipo_usuario = self.cleaned_data.get('tipo_usuario')
        if tipo_usuario:
            # Realize a pesquisa com base no tipo de usuário
            users = TipoUsuario.objects.filter(tipo=tipo_usuario)
            return users
        return TipoUsuario.objects.all()

class PesquisaServicoForm(forms.Form):
    bairro = forms.CharField(max_length=100, required=False)
    duracao_passeio = forms.ChoiceField(choices=[('', 'Qualquer'), ('30m', '30 minutos'), ('1h', '1 hora')], required=False)