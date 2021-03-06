from votacoes import views
from users import views as usersViews
from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import logout_then_login


urlpatterns = [
    path('registrar/',usersViews.registrarUsuarioView.as_view(),name='registrar'),
    path('login/',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    url(r'^logout/$',logout_then_login,{'login_url':'/login/'},name='logout'),

    path('',views.index,name='index'),
    path('listarAlunos/',views.listarAlunos,name='listarAlunos'),
    path('escolherVotacoes/',views.escolherVotacoes,name='escolherVotacoes'),
    path('emAndamento/',views.emAndamento,name='emAndamento'),
    path('pausadas/',views.pausadas,name='pausadas'),
    path('concluidas/',views.concluidas,name='concluidas'),
    path('exibirAluno/<str:cpfAluno>',views.exibirAluno,name='exibirAluno'),
]