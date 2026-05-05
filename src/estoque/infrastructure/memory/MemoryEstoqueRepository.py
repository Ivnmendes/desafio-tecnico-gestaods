from estoque.domain.entities import ItemEstoque
from estoque.domain.exceptions import ProdutoIndisponivelError
from estoque.domain.repositories import IEstoqueRepository
from produto.domain.entities import Produto


class MemoryEstoqueRepository(IEstoqueRepository):

    def __init__(self) -> None:
        self._itens: dict[str, ItemEstoque] = {}

    def obter_item_estoque(self, produto: Produto) -> ItemEstoque:
        if produto.id not in self._itens:
            raise ProdutoIndisponivelError("Produto não encontrado no estoque!")
        return self._itens[produto.id]

    def salvar(self, item_estoque: ItemEstoque) -> ItemEstoque:
        self._itens[item_estoque.produto.id] = item_estoque
        return item_estoque

    def obter_todos_itens_estoque(self) -> list[ItemEstoque]:
        return list(self._itens.values())

    def limpar_estoque(self) -> None:
        self._itens.clear()

    def remover(self, produto: Produto) -> None:
        if produto.id not in self._itens:
            return
        del self._itens[produto.id]

    def filtrar_itens_estoque_preco(
        self, preco_minimo: float = 0.0, preco_maximo: float | None = None
    ) -> list[ItemEstoque]:
        # Este método funciona somente com orm
        # (implementação com persistência em memória
        # não tem acesso ao preço do produto)
        return list(self._itens.values())
