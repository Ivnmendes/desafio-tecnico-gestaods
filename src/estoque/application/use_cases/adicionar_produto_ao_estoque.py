from estoque.domain.entities import ItemEstoque
from estoque.domain.exceptions import ProdutoIndisponivelError
from estoque.domain.repositories import IEstoqueRepository
from produto.domain.repositories import IProdutoRepository


def adicionar_produto_ao_estoque(
    estoque_repo: IEstoqueRepository,
    estoque_produto: IProdutoRepository,
    produto_id: str,
    qtd: int,
) -> ItemEstoque:

    item = estoque_repo.obter_item_estoque(produto_id)

    if item:
        item.ajustar_quantidade(qtd)
    else:
        produto = estoque_produto.obter_produto(produto_id)

        if produto is None:
            raise ProdutoIndisponivelError("Produto não encontrado!")

        novo_item = ItemEstoque(produto, quantidade=qtd)
        item = novo_item

    item_estoque = estoque_repo.salvar(item)

    return item_estoque
