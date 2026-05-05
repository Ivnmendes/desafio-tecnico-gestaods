from estoque.domain.entities import ItemEstoque
from estoque.domain.repositories import IEstoqueRepository
from produto.domain.entities import Produto


def adicionar_produto_ao_estoque(
    estoque_repo: IEstoqueRepository, produto: Produto, qtd: int
) -> ItemEstoque:

    item = estoque_repo.obter_item_estoque(produto.id)

    if item:
        item.ajustar_quantidade(qtd)
    else:
        novo_item = ItemEstoque(produto=produto, quantidade=qtd)
        item = novo_item

    item_estoque = estoque_repo.salvar(item)

    return item_estoque
