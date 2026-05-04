from estoque.domain.entities import ItemEstoque
from estoque.domain.exceptions import ProdutoIndisponivelError
from estoque.domain.repositories import IEstoqueRepository
from estoque.infrastructure.django.models import ItemEstoqueModel


class DjangoEstoqueRepository(IEstoqueRepository):

    def obter_item_estoque(self, produto_id: str) -> ItemEstoque:
        try:
            model = ItemEstoqueModel.objects.get(produto_id=produto_id)
            return ItemEstoque(produto_id=model.produto_id, quantidade=model.quantidade)
        except ItemEstoqueModel.DoesNotExist:
            raise ProdutoIndisponivelError("Produto não encontrado no estoque!")

    def salvar(self, item_estoque: ItemEstoque) -> None:
        ItemEstoqueModel.objects.update_or_create(
            produto_id=item_estoque.produto_id,
            defaults={"quantidade": item_estoque.quantidade},
        )

    def obter_todos_itens_estoque(self) -> list[ItemEstoque]:
        return [
            ItemEstoque(produto_id=model.produto_id, quantidade=model.quantidade)
            for model in ItemEstoqueModel.objects.all()
        ]

    def limpar_estoque(self) -> None:
        ItemEstoqueModel.objects.all().delete()

    def remover(self, produto_id: str) -> None:
        ItemEstoqueModel.objects.filter(produto_id=produto_id).delete()
