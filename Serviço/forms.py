from django import forms
from .models import PrestacaoServicos, InfoPasseio

class PrestacaoServicosForm(forms.ModelForm):
    class Meta:
        model = PrestacaoServicos
        fields = ['bairro', 'duracao_passeio', 'inicio', 'fim']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['inicio'] = forms.ChoiceField(choices=[(f"{i:02d}:00", f"{i:02d}:00") for i in range(6, 23)])
        self.fields['fim'] = forms.ChoiceField(choices=[(f"{i:02d}:00", f"{i:02d}:00") for i in range(6, 23)])

class InfoPasseioForm(forms.ModelForm):
    class Meta:
        model = InfoPasseio
        fields = ['rua', 'numero', 'complemento', 'extras']
