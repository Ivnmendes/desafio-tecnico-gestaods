import uuid

from django.db import models


class ProdutoModel(models.Model):

    class Meta:
        """Configurações da tabela de produtos no banco de dados."""

        db_table = "produto"
        app_label = "produto"
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        ordering = ["-preco"]

    id: models.UUIDField = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    nome: models.CharField = models.CharField(max_length=255)
    preco: models.DecimalField = models.DecimalField(max_digits=10, decimal_places=2)

    def __repr__(self):
        return f"Produto(id={self.id}, nome={self.nome}, preco={self.preco})"

    def __str__(self):
        return f"{self.nome} - R${round(float(self.preco), 2)}"
