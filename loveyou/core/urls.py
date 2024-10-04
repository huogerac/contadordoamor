from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("dapau", views.dapau),
    path("status", views.status),
    path("relacionamentos/add", views.criar_meu_site, name="criar.meu.site"),
    path("vai/<str:nome_site>", views.vai_pro_site, name="vai_pro_site"),
    path("relacionamentos/list", views.list_relacionamentos),
]
