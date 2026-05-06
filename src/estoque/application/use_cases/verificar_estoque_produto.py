from estoque.application.dtos.info_estoque_dto import InfoEstoqueDTO
from estoque.domain.exceptions import ProdutoIndisponivelError
from estoque.domain.repositories import IEstoqueRepository
from produto.domain.repositories import IProdutoRepository


class VerificarEstoqueProdutoUseCase:

    def __init__(
        self, estoque_repo: IEstoqueRepository, produto_repo: IProdutoRepository
    ):
        self.estoque_repo = estoque_repo
        self.produto_repo = produto_repo

    def execute(self, produto_id: str) -> InfoEstoqueDTO:

        item = self.estoque_repo.obter_item_estoque(produto_id)

        if item is None:
            raise ProdutoIndisponivelError("Produto não encontrado no estoque!")

        produto_banco = self.produto_repo.obter_produto(produto_id)
        if produto_banco is None:
            raise ProdutoIndisponivelError("Produto não encontrado no repositório!")

        return InfoEstoqueDTO(
            id=item.produto_id,
            nome=produto_banco.nome,
            valor_individual=produto_banco.preco,
            quantidade=item.quantidade,
        )
