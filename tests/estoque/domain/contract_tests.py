from abc import ABC, abstractmethod

from src.estoque.domain.entities import ItemEstoque
from src.estoque.domain.exceptions import ProdutoIndisponivelError


class EstoqueRepositoryContract(ABC):

    @abstractmethod
    def create_repository(self):
        """Método factory que deve ser sobrescrito."""
        pass

    def test_deve_salvar_e_recuperar_item(self):

        repo = self.create_repository()
        item = ItemEstoque(produto_id="123", quantidade=10)

        repo.salvar(item)
        resultado = repo.obter_item_estoque("123")

        assert resultado.quantidade == 10

    def test_deve_remover_item(self):

        repo = self.create_repository()
        item = ItemEstoque(produto_id="123", quantidade=10)

        repo.salvar(item)
        repo.remover("123")
        resultado = repo.remover("123")

        assert resultado is None

    def test_deve_lancar_erro_ao_obter_item_inexistente(self):

        repo = self.create_repository()

        excecao_lancada = False
        try:
            repo.obter_item_estoque("inexistente")
        except ProdutoIndisponivelError:
            excecao_lancada = True

        assert excecao_lancada is True, "Deveria ter lançado ProdutoIndisponivelError"

    def test_deve_obter_todos_itens(self):

        repo = self.create_repository()
        item1 = ItemEstoque(produto_id="123", quantidade=10)
        item2 = ItemEstoque(produto_id="456", quantidade=5)

        repo.salvar(item1)
        repo.salvar(item2)
        resultado = repo.obter_todos_itens_estoque()

        assert len(resultado) == 2

    def test_deve_limpar_estoque(self):

        repo = self.create_repository()
        item1 = ItemEstoque(produto_id="123", quantidade=10)
        item2 = ItemEstoque(produto_id="456", quantidade=5)

        repo.salvar(item1)
        repo.salvar(item2)
        repo.limpar_estoque()
        resultado = repo.obter_todos_itens_estoque()

        assert len(resultado) == 0
