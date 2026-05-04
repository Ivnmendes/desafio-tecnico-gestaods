from estoque.domain.entities import ItemEstoque
from estoque.domain.exceptions import ProdutoIndisponivelError
from estoque.domain.repositories import IEstoqueRepository


class MemoryEstoqueRepository(IEstoqueRepository):

    def __init__(self) -> None:
        self._itens: dict[str, ItemEstoque] = {}

    def obter_item_estoque(self, produto_id: str) -> ItemEstoque:
        if produto_id not in self._itens:
            raise ProdutoIndisponivelError("Produto não encontrado no estoque!")
        return self._itens[produto_id]

    def salvar(self, item_estoque: ItemEstoque) -> None:
        self._itens[item_estoque.produto_id] = item_estoque

    def obter_todos_itens_estoque(self) -> list[ItemEstoque]:
        return list(self._itens.values())

    def limpar_estoque(self) -> None:
        self._itens.clear()

    def remover(self, produto_id: str) -> None:
        if produto_id not in self._itens:
            return
        del self._itens[produto_id]
