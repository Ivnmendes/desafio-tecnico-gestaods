from estoque.domain.exceptions import ProdutoIndisponivelError
from estoque.domain.repositories import IEstoqueRepository


class AjustarQuantidadeProdutoUseCase:

    def __init__(self, estoque_repo: IEstoqueRepository):
        self.repositorio_estoque = estoque_repo

    def execute(self, produto_id: str, qtd: int) -> None:

        item = self.repositorio_estoque.obter_item_estoque(produto_id)

        if not item:
            raise ProdutoIndisponivelError("Produto não encontrado no estoque!")

        item.ajustar_quantidade(qtd)

        self.repositorio_estoque.salvar(item)
