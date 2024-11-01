import os
import base64
import logging
from datetime import datetime
from django.utils.text import slugify

from ..models import Relacionamento
from ..exceptions import BusinessError

logger = logging.getLogger(__name__)


def criar_meusite(nome_site: str, imagem: str, data_inicio_relacionamento: str) -> dict:
    logger.info("SERVICE add new relacionamento")

    if not isinstance(nome_site, str):
        raise BusinessError("Nome do site inválido. Deve ser um texto")

    nome_site = slugify(nome_site.strip())
    if not nome_site:
        raise BusinessError("Nome do site inválido")

    sites_existente = Relacionamento.objects.filter(nome_site=nome_site)
    if sites_existente:
        hash_unico = base64.urlsafe_b64encode(os.urandom(3)).decode()
        nome_site = slugify(f"{hash_unico}-{nome_site}")

    if data_inicio_relacionamento:
        data_inicio_relacionamento = datetime.strptime(
            data_inicio_relacionamento, "%Y-%m-%d"
        )

    relacionamento = Relacionamento(
        nome_site=nome_site,
        imagem=imagem,
        frase_do_casal="oi",
        data_inicio_relacionamento=data_inicio_relacionamento,
        ativo=True,
    )

    relacionamento.save()
    logger.info("SERVICE relacionamento created.")
    return relacionamento.to_dict_json()


def list_relacionamentos():
    logger.info("SERVICE list relacionamentos")
    relacionamentos_list = Relacionamento.objects.all()
    return [item.to_dict_json() for item in relacionamentos_list]


def get_site(nome_site):
    return Relacionamento.objects.get(nome_site=nome_site)
