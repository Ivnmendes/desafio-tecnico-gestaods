from estoque.domain.exceptions import ProdutoIndisponivelError
from produto.domain.entities import Produto
from produto.domain.repositories import IProdutoRepository


class AlterarValorProdutoUseCase:

    def __init__(self, produto_repo: IProdutoRepository):
        self.produto_repo = produto_repo

    def execute(self, produto_id: str, novo_valor: float) -> Produto:

        produto = self.produto_repo.obter_produto(produto_id)
        if not produto:
            raise ProdutoIndisponivelError("Produto não encontrado.")

        produto.alterar_preco(novo_valor)
        produto = self.produto_repo.salvar(produto)
        return produto
