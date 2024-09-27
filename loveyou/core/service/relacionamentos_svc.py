import logging

from ..models import Relacionamento
from ..exceptions import BusinessError

logger = logging.getLogger(__name__)


def criar_meusite(nome_site: str) -> dict:
    logger.info("SERVICE add new relacionamento")

    if not isinstance(nome_site, str):
        raise BusinessError("Nome do site inválido. Deve ser um texto")

    nome_site = nome_site.strip()
    if not nome_site:
        raise BusinessError("Nome do site inválido")

    relacionamento = Relacionamento(description=nome_site)
    relacionamento.save()
    logger.info("SERVICE relacionamento created.")
    return relacionamento.to_dict_json()


def list_relacionamentos():
    logger.info("SERVICE list relacionamentos")
    relacionamentos_list = Relacionamento.objects.all()
    return [item.to_dict_json() for item in relacionamentos_list]
