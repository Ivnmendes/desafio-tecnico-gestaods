from produto.domain.entities import Produto
from produto.domain.repositories import IProdutoRepository


class MemoryProdutoRepository(IProdutoRepository):

    def __init__(self):
        self.produtos = {}

    def salvar(self, produto) -> None:
        self.produtos[produto.id] = produto

    def obter_produto(self, produto_id) -> Produto | None:
        return self.produtos.get(produto_id, None)

    def obter_todos_produtos(self) -> list[Produto]:
        return list(self.produtos.values())

    def remover(self, produto_id) -> None:
        if produto_id in self.produtos:
            del self.produtos[produto_id]

    def buscar_por_ids(self, produto_ids) -> list[Produto]:
        return [self.produtos[pid] for pid in produto_ids if pid in self.produtos]
