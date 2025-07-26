from django.contrib import admin
from django.urls import path
from daycare import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

urlpatterns = [
    # 🔧 Admin
    path('admin/', admin.site.urls),

    # 🌐 Página inicial
    path('', lambda request: redirect('login')),
    path('home/', login_required(views.home), name='home'),

    # 🔐 Autenticação
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('registrar/', views.registrar_usuario, name='registrar'),

    # 🔒 Recuperação de senha
    path('senha/resetar/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    path('senha/resetar/enviado/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('senha/resetar/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('senha/resetar/completo/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),

    # ✅ Cadastros
    path('cadastro_tutor/', views.cadastro_tutor, name='cadastro_tutor'),
    path('cadastro_pet/', views.cadastro_pet, name='cadastro_pet'),
    path('cadastro_servico/', views.cadastro_servico, name='cadastro_servico'),
    path('agendamento/', views.agendamento, name='agendamento'),
    path('agendamento/<int:agendamento_id>/', views.agendamento, name='editar_agendamento'),

    # 👤 Tutores
    path('tutores/', views.listar_tutores, name='listar_tutores'),
    path('tutores/editar/<int:tutor_id>/', views.editar_tutor, name='editar_tutor'),
    path('tutores/excluir/<int:tutor_id>/', views.excluir_tutor, name='excluir_tutor'),
    path('tutores/<int:tutor_id>/', views.detalhes_tutor, name='detalhes_tutor'),

    # 👤 Usuários
    path('usuarios/', views.listar_usuarios, name='listar_usuarios'),
    path('usuarios/<int:usuario_id>/editar/', views.editar_usuario, name='editar_usuario'),
    path('usuarios/<int:usuario_id>/excluir/', views.excluir_usuario, name='excluir_usuario'),

    # 🐶 Pets
    path('pets/', views.listar_pets, name='listar_pets'),
    path('pets/editar/<int:pet_id>/', views.editar_pet, name='editar_pet'),
    path('pets/excluir/<int:pet_id>/', views.excluir_pet, name='excluir_pet'),

    # 🛠️ Serviços
    path('servicos/', views.listar_servicos, name='listar_servicos'),
    path('servicos/editar/<int:servicos_id>/', views.editar_servicos, name='editar_servicos'),
    path('servicos/excluir/<int:servicos_id>/', views.excluir_servicos, name='excluir_servicos'),

    # 📆 Agendamentos
    path('agendamentos/', views.listar_agendamentos, name='listar_agendamentos'),
    path('agendamentos/editar/<int:agendamentos_id>/', views.editar_agendamentos, name='editar_agendamentos'),
    path('agendamentos/excluir/<int:agendamentos_id>/', views.excluir_agendamentos, name='excluir_agendamentos'),

    # 📊 Relatórios
    path('relatorios/', views.relatorios, name='relatorios'),
    path('relatorios/excel/', views.exportar_relatorio_excel, name='exportar_relatorio_excel'),

    # 📄 Nota de Atendimento
    path('nota/<int:agendamento_id>/', views.nota_atendimento, name='nota_atendimento'),
    path('nota/<int:agendamento_id>/', views.gerar_nota, name='gerar_nota'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
