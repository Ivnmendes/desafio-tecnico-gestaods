from abc import abstractmethod

from estoque.domain.entities import ItemEstoque
from estoque.domain.repositories import IEstoqueRepository


class MemoryEstoqueRepository(IEstoqueRepository):

    def __init__(self) -> None:
        self._itens: dict[str, ItemEstoque] = {}

    def obter_item_estoque(self, produto_id: str) -> ItemEstoque | None:
        if produto_id not in self._itens:
            return None
        return self._itens[produto_id]

    def salvar(self, item_estoque: ItemEstoque) -> ItemEstoque:
        self._itens[item_estoque.produto.id] = item_estoque
        return item_estoque

    def obter_todos_itens_estoque(self) -> list[ItemEstoque]:
        return list(self._itens.values())

    def limpar_estoque(self) -> None:
        self._itens.clear()

    def remover(self, produto_id: str) -> None:
        if produto_id not in self._itens:
            return None
        del self._itens[produto_id]

    @abstractmethod
    def filtrar_itens_estoque_preco(
        self, preco_minimo: float = 0.0, preco_maximo: float | None = None
    ) -> list[ItemEstoque]:
        # Este método funciona somente com orm
        # (implementação com persistência em memória
        # não tem acesso ao preço do produto)
        pass
