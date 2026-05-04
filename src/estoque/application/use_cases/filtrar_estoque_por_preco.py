from produto.domain.repositories import IProdutoRepository


def filtrar_estoque_por_preco(
    repositorio_produto: IProdutoRepository,
    preco_minimo: float = 0.0,
    preco_maximo: float | None = None,
):

    if preco_minimo < 0:
        raise ValueError("O preço mínimo não pode ser negativo.")
    if preco_maximo is not None and preco_maximo < 0:
        raise ValueError("O preço máximo não pode ser negativo.")
    if preco_maximo is not None and preco_minimo > preco_maximo:
        raise ValueError("O preço mínimo não pode ser maior que o preço máximo.")

    return repositorio_produto.filtrar_produtos_preco(preco_minimo, preco_maximo)
