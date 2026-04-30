from src.estoque.domain.entities import ItemEstoque
from src.estoque.domain.exceptions import ProdutoIndisponivelError
from src.estoque.domain.repositories import IEstoqueRepository


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

    # def filtrar_estoque_por_valor(
    #     self, min_valor: float = 0, max_valor: float = None
    # ) -> list[ItemEstoque]:

    #     if max_valor is not None and (min_valor > max_valor):
    #         raise ValueError(


#               "Filtros inválidos: "
#               "O valor mínimo não pode ser maior que o valor máximo."
#         )

#     if min_valor < 0:
#         raise ValueError(
#               "Filtros inválidos: "
#               " O valor mínimo não pode ser negativo.")

#     produtos_filtrados = []

#     for item in self._itens.values():
#         if item.produto.preco.valor < min_valor:
#             continue

#         if max_valor is not None and item.produto.preco.valor > max_valor:
#             continue

#         produtos_filtrados.append(item)

#     return produtos_filtrados
