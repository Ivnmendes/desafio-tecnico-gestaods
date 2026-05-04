from produto.domain.entities import Produto
from produto.domain.repositories import IProdutoRepository


def criar_produto(
    nome: str, preco: float, produto_repository: IProdutoRepository
) -> Produto:

    produto = Produto(nome=nome, preco=preco)
    produto_banco = produto_repository.salvar(produto)
    return produto_banco
