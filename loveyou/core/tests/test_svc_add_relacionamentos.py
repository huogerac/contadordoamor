import pytest

from loveyou.core.models import Relacionamento
from loveyou.core.service import relacionamentos_svc
from loveyou.core.exceptions import BusinessError


@pytest.mark.django_db
def test_deve_inserir_uma_nova_tarefa():
    new_item = relacionamentos_svc.criar_meusite("ABC")

    item = Relacionamento.objects.all().first()

    assert item.id == new_item.get("id")
    assert item.description == new_item.get("description")


@pytest.mark.django_db
def test_deve_retornar_um_erro_ao_cadastrar_item_com_espacos_na_descricao():
    # Quando tentamos adicionar item sem valor
    with pytest.raises(BusinessError) as error:
        relacionamentos_svc.criar_meusite("    ")

    # Então
    assert str(error.value) == "Nome do site inválido"


@pytest.mark.django_db
def test_deve_aceitar_apenas_tipo_string_na_descricao():
    # Quando tentamos adicionar item sem valor
    with pytest.raises(BusinessError) as error:
        relacionamentos_svc.criar_meusite(1000)

    # Então
    assert str(error.value) == "Nome do site inválido. Deve ser um texto"
