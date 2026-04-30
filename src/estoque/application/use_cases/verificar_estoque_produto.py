from estoque.application.dtos.InfoEstoqueDTO import InfoEstoqueDTO
from estoque.domain.exceptions import ProdutoIndisponivelError
from estoque.domain.repositories import IEstoqueRepository
from produto.domain.repositories import IProdutoRepository


def verificar_estoque_produto(
    estoque_repo: IEstoqueRepository, produto_repo: IProdutoRepository, produto_id: str
) -> InfoEstoqueDTO:
    item = estoque_repo.obter_item_estoque(produto_id)

    if item is None:
        raise ProdutoIndisponivelError("Produto não encontrado no estoque!")

    produto = produto_repo.obter_produto(produto_id)
    if produto is None:
        raise ProdutoIndisponivelError("Produto não encontrado no repositório!")

    return InfoEstoqueDTO(
        id=item.produto_id,
        nome=produto.nome,
        valor_individual=produto.preco,
        quantidade=item.quantidade,
    )
