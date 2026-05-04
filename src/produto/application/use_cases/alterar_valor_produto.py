from produto.domain.repositories import IProdutoRepository


def alterar_valor_produto(
    produto_id: str, novo_valor: float, produto_repository: IProdutoRepository
):

    produto = produto_repository.obter_produto(produto_id)
    if not produto:
        raise ValueError("Produto não encontrado.")

    produto.alterar_preco(novo_valor)
    produto_repository.salvar(produto)
