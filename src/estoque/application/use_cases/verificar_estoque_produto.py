from estoque.application.dtos.InfoEstoqueDTO import InfoEstoqueDTO
from estoque.domain.exceptions import ProdutoIndisponivelError
from estoque.domain.repositories import IEstoqueRepository
from produto.domain.entities import Produto
from produto.domain.repositories import IProdutoRepository


def verificar_estoque_produto(
    estoque_repo: IEstoqueRepository, produto_repo: IProdutoRepository, produto: Produto
) -> InfoEstoqueDTO:

    item = estoque_repo.obter_item_estoque(produto.id)

    if item is None:
        raise ProdutoIndisponivelError("Produto não encontrado no estoque!")

    produto_banco = produto_repo.obter_produto(produto.id)
    if produto_banco is None:
        raise ProdutoIndisponivelError("Produto não encontrado no repositório!")

    return InfoEstoqueDTO(
        id=item.produto_id,
        nome=produto_banco.nome,
        valor_individual=produto_banco.preco,
        quantidade=item.quantidade,
    )
