from django.urls import path
from django.contrib.auth import views as auth_views
from . import views 
from django.contrib.auth.views import logout_then_login
from django.conf.urls import url
urlpatterns = [
    #path('',views.login,name='login'),
    path('registrar/',views.registrarUsuarioView.as_view(),name='registrar'),
    path('login/',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    url(r'^logout/$',logout_then_login,{'login_url':'/login/'},name='logout'),
    path('',views.index,name='index'),
]