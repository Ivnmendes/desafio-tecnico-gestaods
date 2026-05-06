from estoque.domain.repositories import IEstoqueRepository


class TotalProdutosEstoqueUseCase:

    def __init__(self, estoque_repo: IEstoqueRepository):
        self.repositorio_estoque = estoque_repo

    def execute(self):
        itens = self.repositorio_estoque.obter_todos_itens_estoque()
        return sum(item.quantidade for item in itens)
