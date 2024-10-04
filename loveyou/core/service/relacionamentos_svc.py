import logging

from django.utils.text import slugify

from ..models import Relacionamento
from ..exceptions import BusinessError

logger = logging.getLogger(__name__)


def criar_meusite(nome_site: str, imagem: str) -> dict:
    logger.info("SERVICE add new relacionamento")

    if not isinstance(nome_site, str):
        raise BusinessError("Nome do site inválido. Deve ser um texto")

    nome_site = slugify(nome_site.strip())
    if not nome_site:
        raise BusinessError("Nome do site inválido")

    relacionamento = Relacionamento(
        nome_site=nome_site,
        imagem=imagem,
        frase_do_casal="oi",
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
