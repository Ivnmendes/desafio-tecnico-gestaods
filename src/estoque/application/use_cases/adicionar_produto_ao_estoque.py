from estoque.domain.entities import ItemEstoque
from estoque.domain.repositories import IEstoqueRepository


def adicionar_produto_ao_estoque(
    estoque_repo: IEstoqueRepository, produto_id: str, qtd: int
) -> None:

    item = estoque_repo.obter_item_estoque(produto_id)

    if item:
        item.ajustar_quantidade(qtd)
    else:
        novo_item = ItemEstoque(produto_id=produto_id, quantidade=qtd)
        item = novo_item

    estoque_repo.salvar(item)
