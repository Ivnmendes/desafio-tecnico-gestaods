import uuid

from django.db import models

from produto.infrastructure.django_models import ProdutoModel


class ItemEstoqueModel(models.Model):

    class Meta:
        """Configurações da tabela de itens de estoque no banco de dados."""

        db_table = "item_estoque"
        app_label = "estoque"
        verbose_name = "Item de Estoque"
        verbose_name_plural = "Itens de Estoque"

    id: models.UUIDField = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    produto: models.ForeignKey = models.ForeignKey(
        ProdutoModel, on_delete=models.CASCADE, related_name="itens_estoque"
    )
    quantidade: models.IntegerField = models.IntegerField()

    def __repr__(self):
        return (
            f"ItemEstoque("
            f"id={self.id},"
            f"produto={self.produto.id},"
            f"quantidade={self.quantidade}"
            f")"
        )

    def __str__(self):
        return f"Produto: {self.produto.nome} - Quantidade: {self.quantidade}"
