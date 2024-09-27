# coding: utf-8
import logging
import os

from django.db import connection
from django.http import JsonResponse
from .exceptions import BusinessError
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .service import relacionamentos_svc

logger = logging.getLogger(__name__)


def dapau(request, error: str = None):
    """
    Retorna um erro real para ajudar nos testes
    """
    if error and error.upper() == "BUSINESS":
        raise BusinessError("BusinessError")
    raise Exception("break on purpose")


def status(request):
    """
    Retorna o estado atual da aplicação
    """
    cursor = connection.cursor()
    cursor.execute("""SELECT 1+1""")
    row = cursor.fetchone()
    git_hash = os.getenv("GIT_HASH", "?")
    return JsonResponse(
        {
            "status": "ok",
            "db": "ok" if row == (2,) else "error",
            "git_hash": git_hash,
        }
    )


@csrf_exempt
def criar_meu_site(request):
    """Adiciona Relacionamento"""
    logger.info("API add new relacionamento.")
    # body = json.loads(request.body)
    body = request.POST
    nome_site = body.get("nome_site")

    if not nome_site:
        raise ValueError("body.relacionamento.nome_site: Field required (missing)")

    if type(nome_site) not in [str]:
        raise ValueError(
            "body.relacionamento.nome_site: Input should be a valid string (string_type)"
        )

    nome_site = str(nome_site)
    if len(nome_site) <= 2:
        raise ValueError(
            "body.relacionamento.nome_site: Value error, It must be at least 3 characteres long. (value_error)"
        )

    novo_site = relacionamentos_svc.criar_meusite(nome_site)
    print(novo_site)
    # context = {"novo_site": novo_site}
    print("chegueo")
    # return JsonResponse(new_relacionamento, status=201)
    # return render(request, "site_do_casal", context)
    url = reverse("vai_pro_site", kwargs={"nome_site": str(novo_site)})

    return redirect(url)


@csrf_exempt
def vai_pro_site(request, nome_site):
    context = {"nome_site": nome_site}
    print("cheguei aqui")
    return render(request, "core/site_do_casal.html", context)


@require_http_methods(["GET"])
def list_relacionamentos(request):
    """Lista Relacionamentos"""
    logger.info("API list relacionamentos")
    relacionamentos = relacionamentos_svc.list_relacionamentos()
    return JsonResponse({"relacionamentos": relacionamentos})
