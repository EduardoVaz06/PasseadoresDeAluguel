from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TipoUsuario(models.Model):
    TIPOS_USUARIO = (
        ('usuario', 'Usuário'),
        ('passeador', 'Passeador'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=10, choices=TIPOS_USUARIO)
    telefone = models.CharField(max_length=15)
    image = models.ImageField(default='default.jpg', upload_to='imagens_perfil')
    

    def __str__(self):
        return f"{self.user.username} - {self.tipo}"
