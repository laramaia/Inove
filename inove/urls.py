# arquivo responsável por mapear urls
from django.contrib import admin
from django.urls import path, include
from exemplo import views

# solicitações 'solicitacao/' são feitas e usuário é levado para caminho correto
urlpatterns = [
    path('admin/', admin.site.urls),
    path('acesso/', include('autenticacao.usuarios.urls')),
    path('exemplo/', views.index)
]
