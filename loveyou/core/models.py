from django.db import models


class Relacionamento(models.Model):
    nome_site = models.CharField(max_length=128, unique=True, default="")
    data_inicio_relacionamento = models.DateField(null=True, blank=True)
    imagem = models.TextField(null=True, blank=True)
    frase_do_casal = models.TextField(null=True, blank=True)
    ativo = models.BooleanField(default=False)

    def to_dict_json(self):
        return {
            "id": self.id,
            "nome_site": self.nome_site,
            "frase_do_casal": self.frase_do_casal,
            "ativo": self.ativo,
        }
