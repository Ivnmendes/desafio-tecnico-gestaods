from produto.domain.entities import Produto
from produto.domain.repositories import IProdutoRepository


class CriarProdutoUseCase:

    def __init__(self, produto_repo: IProdutoRepository):
        self.produto_repo = produto_repo

    def execute(self, nome: str, preco: float) -> Produto:

        produto = Produto(nome=nome, preco=preco)
        produto_banco = self.produto_repo.salvar(produto)

        return produto_banco
