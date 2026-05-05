import uuid
from abc import ABC, abstractmethod

from estoque.domain.entities import ItemEstoque
from estoque.domain.exceptions import ProdutoIndisponivelError
from produto.domain.entities import Produto


class EstoqueRepositoryContract(ABC):

    @abstractmethod
    def create_repository(self):
        """Método factory que deve ser sobrescrito."""
        pass

    @abstractmethod
    def setup_produto(self, produto: Produto) -> None:
        """Garante que o produto exista no banco/memória antes de criar o estoque."""
        pass

    def test_deve_salvar_e_recuperar_item(self):

        repo = self.create_repository()
        id_produto = str(uuid.uuid4())
        produto = Produto(id=id_produto, nome="Produto Teste", preco=10.0)

        self.setup_produto(produto)

        item = ItemEstoque(produto=produto, quantidade=10)

        repo.salvar(item)
        resultado = repo.obter_item_estoque(produto)

        assert (
            resultado.quantidade == 10
        ), "A quantidade recuperada deve ser igual à quantidade salva"
        assert (
            str(resultado.produto_id) == id_produto
        ), "O ID do produto recuperado deve ser igual ao ID do produto salvo"

    def test_deve_remover_item(self):

        repo = self.create_repository()
        id_produto = str(uuid.uuid4())
        produto = Produto(id=id_produto, nome="Produto Teste", preco=10.0)

        self.setup_produto(produto)

        item = ItemEstoque(produto=produto, quantidade=10)

        repo.salvar(item)
        repo.remover(produto)

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
        produto1 = Produto(id=id1, nome="Produto 1", preco=10.0)
        id2 = str(uuid.uuid4())
        produto2 = Produto(id=id2, nome="Produto 2", preco=5.0)

        self.setup_produto(produto1)
        self.setup_produto(produto2)

        item1 = ItemEstoque(produto=produto1, quantidade=10)
        item2 = ItemEstoque(produto=produto2, quantidade=5)

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

        produto1 = Produto(id=id1, nome="Produto 1", preco=10.0)
        produto2 = Produto(id=id2, nome="Produto 2", preco=5.0)

        self.setup_produto(produto1)
        self.setup_produto(produto2)

        item1 = ItemEstoque(produto=produto1, quantidade=10)
        item2 = ItemEstoque(produto=produto2, quantidade=5)

        repo.salvar(item1)
        repo.salvar(item2)
        repo.limpar_estoque()

        excecao_lancada = False
        try:
            repo.obter_item_estoque(str(uuid.uuid4()))
        except ProdutoIndisponivelError:
            excecao_lancada = True

        assert excecao_lancada is True, "Deveria ter lançado ProdutoIndisponivelError"

    def test_deve_filtrar_itens_por_preco(self):

        repo = self.create_repository()

        id1 = str(uuid.uuid4())
        produto1 = Produto(id=id1, nome="Produto 1", preco=10.0)
        id2 = str(uuid.uuid4())
        produto2 = Produto(id=id2, nome="Produto 2", preco=20.0)
        id3 = str(uuid.uuid4())
        produto3 = Produto(id=id3, nome="Produto 3", preco=30.0)

        self.setup_produto(produto1)
        self.setup_produto(produto2)
        self.setup_produto(produto3)

        item1 = ItemEstoque(produto=produto1, quantidade=10)
        item2 = ItemEstoque(produto=produto2, quantidade=5)
        item3 = ItemEstoque(produto=produto3, quantidade=2)

        repo.salvar(item1)
        repo.salvar(item2)
        repo.salvar(item3)

        resultado = repo.filtrar_itens_estoque_preco(
            preco_minimo=15.0, preco_maximo=25.0
        )

        assert len(resultado) == 1, "Deveria ter retornado apenas 1 item no estoque"
        assert id2 in [
            str(item.produto_id) for item in resultado
        ], "O ID do item filtrado deveria estar presente no resultado"

    def test_deve_filtrar_itens_por_preco_com_preco_maximo_none(self):

        repo = self.create_repository()

        id1 = str(uuid.uuid4())
        id2 = str(uuid.uuid4())
        id3 = str(uuid.uuid4())

        produto1 = Produto(id=id1, nome="Produto 1", preco=10.0)
        produto2 = Produto(id=id2, nome="Produto 2", preco=20.0)
        produto3 = Produto(id=id3, nome="Produto 3", preco=30.0)

        self.setup_produto(produto1)
        self.setup_produto(produto2)
        self.setup_produto(produto3)

        item1 = ItemEstoque(produto=produto1, quantidade=10)
        item2 = ItemEstoque(produto=produto2, quantidade=5)
        item3 = ItemEstoque(produto=produto3, quantidade=2)

        repo.salvar(item1)
        repo.salvar(item2)
        repo.salvar(item3)

        resultado = repo.filtrar_itens_estoque_preco(
            preco_minimo=15.0, preco_maximo=None
        )

        assert len(resultado) == 2, "Deveria ter retornado 2 itens no estoque"
        assert id2 in [
            str(item.produto_id) for item in resultado
        ], "O ID do segundo item filtrado deveria estar presente no resultado"
        assert id3 in [
            str(item.produto_id) for item in resultado
        ], "O ID do terceiro item filtrado deveria estar presente no resultado"
