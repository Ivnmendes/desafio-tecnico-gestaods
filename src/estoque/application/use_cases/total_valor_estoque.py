from estoque.domain.repositories import IEstoqueRepository
from produto.domain.repositories import IProdutoRepository


class TotalValorEstoqueUseCase:

    def __init__(
        self,
        estoque_repo: IEstoqueRepository,
        produto_repo: IProdutoRepository,
    ):
        self.repositorio_estoque = estoque_repo
        self.repositorio_produto = produto_repo

    def execute(self):

        itens_estoque = self.repositorio_estoque.obter_todos_itens_estoque()

        ids = [item.produto_id for item in itens_estoque]
        produtos = self.repositorio_produto.buscar_por_ids(ids)

        mapa_precos = {p.id: float(p.preco) for p in produtos}

        total = 0.0
        for item in itens_estoque:
            preco = mapa_precos.get(item.produto_id, 0)
            total += preco * item.quantidade

        return total
