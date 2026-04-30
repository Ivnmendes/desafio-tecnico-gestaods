from estoque.domain.repositories import IEstoqueRepository
from produto.domain.repositories import IProdutoRepository


def total_valor_estoque(
    repositorio_estoque: IEstoqueRepository, repositorio_produto: IProdutoRepository
) -> float:

    itens_estoque = repositorio_estoque.obter_todos_itens_estoque()

    ids = [item.produto_id for item in itens_estoque]
    produtos = repositorio_produto.buscar_por_ids(ids)

    mapa_precos = {p.id: p.preco for p in produtos}

    total = 0.0
    for item in itens_estoque:
        preco = mapa_precos.get(item.produto_id, 0)
        total += preco * item.quantidade

    return total
