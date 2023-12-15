from django.contrib import admin
from django.urls import path
from Login import views as login_views
from Agenda import views as agenda_views
from Perfil import views as perfil_views
from django.conf import settings
from django.conf.urls.static import static
from Agenda.views import agenda_passeador
from Serviço import views as serviço_views
from Avaliação import views as avaliação_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registrar/', login_views.registrar, name='registrar'),
    path('', login_views.logar, name='login'),
    path('infos/', login_views.infos, name='infos'),
    path('logout/', login_views.deslogar, name='logout'),
    path('home/usuario', login_views.home_usuario, name='home_usuario'),
    path('home/passeador', login_views.home_passeador, name='home_passeador'),
    path('perfil/', perfil_views.visualizar_perfil, name='perfil'),
    path('perfil_passeador/<int:user_id>/', perfil_views.perfil_passeador, name='perfil_passeador'),
    path('perfil_passeador_self/<int:user_id>/', perfil_views.perfil_passeador_self, name='perfil_passeador_self'),
    path('horarios/<int:passeador_id>/', login_views.horarios_view, name='horarios'),
    path('selecionar_horario/', login_views.selecionar_horario, name='selecionar_horario'),
    path('editar_perfil/', perfil_views.editar_perfil, name='editar_perfil'),
    path('editar_perfil_passeador/', perfil_views.editar_perfil_passeador, name='editar_perfil_passeador'),
    path('agenda_passeador/<int:user_id>/', agenda_passeador, name='agenda_passeador'),
    path('passeios_finalizados/<int:user_id>/', agenda_views.passeios_finalizados, name='passeios_finalizados'),
    path('passeios_solicitados/<int:user_id>/', agenda_views.passeios_solicitados, name='passeios_solicitados'),
    path('aceitar_passeio/<int:horario_id>/', agenda_views.aceitar_passeio, name='aceitar_passeio'),
    path('recusar_passeio/<int:horario_id>/', agenda_views.recusar_passeio, name='recusar_passeio'),
    path('finalizar_passeio/<int:horario_id>/', agenda_views.finalizar_passeio, name='finalizar_passeio'),
    path('agenda_usuario/<int:user_id>/', agenda_views.agenda_usuario, name='agenda_usuario'),
    path('passeios_finalizados_user/<int:user_id>/', agenda_views.passeios_finalizados_user, name='passeios_finalizados_user'),
    path('passeios_solicitados_user/<int:user_id>/', agenda_views.passeios_solicitados_user, name='passeios_solicitados_user'),
    path('adicionar_info_passeio/', serviço_views.adicionar_info_passeio, name='adicionar_info_passeio'),
    path('info_passeio/<int:id_passeio_id>/', login_views.info_passeio, name='info_passeio'),
    #testes
    path('guardar/', login_views.teste_view, name='teste'),
    path('avaliar_passeador/<int:id_solicitacao>/', avaliação_views.avaliar_passeador, name='avaliar_passeador'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)