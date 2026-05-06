from estoque.domain.entities import ItemEstoque
from estoque.domain.exceptions import ProdutoIndisponivelError
from estoque.domain.repositories import IEstoqueRepository
from produto.domain.repositories import IProdutoRepository


class AdicionarProdutoAoEstoqueUseCase:

    def __init__(
        self,
        estoque_repo: IEstoqueRepository,
        produto_repo: IProdutoRepository,
    ):
        self.estoque_repo = estoque_repo
        self.estoque_produto = produto_repo

    def execute(
        self,
        produto_id: str,
        qtd: int,
    ) -> ItemEstoque:

        item = self.estoque_repo.obter_item_estoque(produto_id)

        if item:
            item.ajustar_quantidade(qtd)
        else:
            produto = self.estoque_produto.obter_produto(produto_id)

            if produto is None:
                raise ProdutoIndisponivelError("Produto não encontrado!")

            novo_item = ItemEstoque(produto, quantidade=qtd)
            item = novo_item

        item_estoque = self.estoque_repo.salvar(item)

        return item_estoque
