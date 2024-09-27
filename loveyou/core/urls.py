from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path("", TemplateView.as_view(template_name="core/home.html")),
    path("dapau", views.dapau),
    path("status", views.status),
    path("relacionamentos/add", views.criar_meu_site, name="criar.meu.site"),
    path("vai/<str:nome_site>", views.vai_pro_site, name="vai_pro_site"),
    path("relacionamentos/list", views.list_relacionamentos),
]
