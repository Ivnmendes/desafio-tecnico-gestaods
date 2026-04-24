from src.estoque.domain.exceptions import ProdutoIndisponivelError
from src.estoque.domain.repositories import IEstoqueRepository


def ajustar_quantidade_produto(
    repositorio_estoque: IEstoqueRepository, produto_id: str, qtd: int
) -> None:

    item = repositorio_estoque.obter_item_estoque(produto_id)

    if not item:
        raise ProdutoIndisponivelError("Produto não encontrado no estoque!")

    item.ajustar_quantidade(qtd)
