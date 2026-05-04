import uuid
from abc import ABC, abstractmethod

from estoque.domain.entities import ItemEstoque
from estoque.domain.exceptions import ProdutoIndisponivelError


class EstoqueRepositoryContract(ABC):

    @abstractmethod
    def create_repository(self):
        """Método factory que deve ser sobrescrito."""
        pass

    @abstractmethod
    def setup_produto(self, id_produto: str, nome_produto: str, preco: float) -> None:
        """Garante que o produto exista no banco/memória antes de criar o estoque."""
        pass

    def test_deve_salvar_e_recuperar_item(self):

        repo = self.create_repository()
        id_produto = str(uuid.uuid4())

        self.setup_produto(id_produto, "Produto Teste", 10.0)

        item = ItemEstoque(produto_id=id_produto, quantidade=10)

        repo.salvar(item)
        resultado = repo.obter_item_estoque(id_produto)

        assert (
            resultado.quantidade == 10
        ), "A quantidade recuperada deve ser igual à quantidade salva"
        assert (
            str(resultado.produto_id) == id_produto
        ), "O ID do produto recuperado deve ser igual ao ID do produto salvo"

    def test_deve_remover_item(self):

        repo = self.create_repository()
        id_produto = str(uuid.uuid4())

        self.setup_produto(id_produto, "Produto Teste", 10.0)

        item = ItemEstoque(produto_id=id_produto, quantidade=10)

        repo.salvar(item)
        repo.remover(id_produto)

        excecao_lancada = False
        try:
            repo.obter_item_estoque(str(uuid.uuid4()))
        except ProdutoIndisponivelError:
            excecao_lancada = True

        assert excecao_lancada is True, "Deveria ter lançado ProdutoIndisponivelError"

    def test_deve_remover_item_inexistente_sem_erro(self):

        repo = self.create_repository()
        id_produto = str(uuid.uuid4())

        try:
            repo.remover(id_produto)
        except Exception as e:
            assert False, f"Não deveria ter lançado nenhuma exceção, mas lançou: {e}"

    def test_deve_lancar_erro_ao_obter_item_inexistente(self):

        repo = self.create_repository()

        excecao_lancada = False
        try:
            repo.obter_item_estoque(str(uuid.uuid4()))
        except ProdutoIndisponivelError:
            excecao_lancada = True

        assert excecao_lancada is True, "Deveria ter lançado ProdutoIndisponivelError"

    def test_deve_obter_todos_itens(self):

        repo = self.create_repository()

        id1 = str(uuid.uuid4())
        id2 = str(uuid.uuid4())

        self.setup_produto(id1, "Produto 1", 10.0)
        self.setup_produto(id2, "Produto 2", 5.0)

        item1 = ItemEstoque(produto_id=id1, quantidade=10)
        item2 = ItemEstoque(produto_id=id2, quantidade=5)

        repo.salvar(item1)
        repo.salvar(item2)
        resultado = repo.obter_todos_itens_estoque()

        assert len(resultado) == 2, "Deveria ter retornado 2 itens no estoque"
        assert id1 in [
            str(item.produto_id) for item in resultado
        ], "O ID do primeiro item deveria estar presente no resultado"
        assert id2 in [
            str(item.produto_id) for item in resultado
        ], "O ID do segundo item deveria estar presente no resultado"

    def test_deve_limpar_estoque(self):

        repo = self.create_repository()
        id1 = str(uuid.uuid4())
        id2 = str(uuid.uuid4())

        self.setup_produto(id1, "Produto 1", 10.0)
        self.setup_produto(id2, "Produto 2", 5.0)

        item1 = ItemEstoque(produto_id=id1, quantidade=10)
        item2 = ItemEstoque(produto_id=id2, quantidade=5)

        repo.salvar(item1)
        repo.salvar(item2)
        repo.limpar_estoque()

        excecao_lancada = False
        try:
            repo.obter_item_estoque(str(uuid.uuid4()))
        except ProdutoIndisponivelError:
            excecao_lancada = True

        assert excecao_lancada is True, "Deveria ter lançado ProdutoIndisponivelError"
