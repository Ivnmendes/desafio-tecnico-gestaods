from estoque.domain.entities import ItemEstoque
from estoque.domain.repositories import IEstoqueRepository
from estoque.infrastructure.django.models import ItemEstoqueModel


class DjangoEstoqueRepository(IEstoqueRepository):

    def obter_item_estoque(self, produto_id: str) -> ItemEstoque | None:
        try:
            model = ItemEstoqueModel.objects.get(produto_id=produto_id)
            return ItemEstoque(produto=model.produto, quantidade=model.quantidade)
        except ItemEstoqueModel.DoesNotExist:
            return None

    def salvar(self, item_estoque: ItemEstoque) -> ItemEstoque:
        model, _ = ItemEstoqueModel.objects.update_or_create(
            produto_id=item_estoque.produto_id,
            defaults={"quantidade": item_estoque.quantidade},
        )

        return model

    def obter_todos_itens_estoque(self) -> list[ItemEstoque]:
        return [
            ItemEstoque(produto=model.produto, quantidade=model.quantidade)
            for model in ItemEstoqueModel.objects.all()
        ]

    def limpar_estoque(self) -> None:
        ItemEstoqueModel.objects.all().delete()

    def remover(self, produto_id: str) -> None:
        ItemEstoqueModel.objects.filter(produto_id=produto_id).delete()

    def filtrar_itens_estoque_preco(
        self, preco_minimo: float = 0.0, preco_maximo: float | None = None
    ) -> list[ItemEstoque]:

        filters = {"produto__preco__gte": preco_minimo}
        if preco_maximo is not None:
            filters["produto__preco__lte"] = preco_maximo

        return [
            ItemEstoque(produto=model.produto, quantidade=model.quantidade)
            for model in ItemEstoqueModel.objects.filter(**filters)
        ]
