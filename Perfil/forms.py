from django import forms
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserChangeForm
from Login.models import TipoUsuario
from .widgets import CustomClearableFileInput  # Certifique-se de ajustar o caminho correto para o seu widget

class CustomUserChangeForm(UserChangeForm):
    photo = forms.ImageField(required=False, widget=CustomClearableFileInput)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class UserProfileForm(forms.ModelForm):
    image = forms.ImageField(required=False, widget=CustomClearableFileInput)

    class Meta:
        model = TipoUsuario
        fields = ('telefone', 'image')
