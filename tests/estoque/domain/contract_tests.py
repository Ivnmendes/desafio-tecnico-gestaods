from abc import ABC, abstractmethod
from unittest import TestCase

from src.estoque.domain.entities import ItemEstoque
from src.estoque.domain.exceptions import ProdutoIndisponivelError


class EstoqueRepositoryContract(ABC, TestCase):

    @abstractmethod
    def create_repository(self):
        """Método factory que deve ser sobrescrito."""
        pass

    def test_deve_salvar_e_recuperar_item(self):

        repo = self.create_repository()
        item = ItemEstoque(produto_id="123", quantidade=10)

        repo.salvar(item)
        resultado = repo.obter_por_id("123")

        assert resultado.quantidade == 10

    def test_deve_remover_item(self):

        repo = self.create_repository()
        item = ItemEstoque(produto_id="123", quantidade=10)

        repo.salvar(item)
        repo.remover("123")
        resultado = repo.obter_por_id("123")

        assert resultado is None

    def test_deve_lancar_erro_ao_obter_item_inexistente(self):

        repo = self.create_repository()

        with self.assertRaises(ProdutoIndisponivelError):
            repo.obter_por_id("inexistente")

    def test_deve_obter_todos_itens(self):

        repo = self.create_repository()
        item1 = ItemEstoque(produto_id="123", quantidade=10)
        item2 = ItemEstoque(produto_id="456", quantidade=5)

        repo.salvar(item1)
        repo.salvar(item2)
        resultado = repo.obter_todos_itens()

        assert len(resultado) == 2

    def test_deve_limpar_estoque(self):

        repo = self.create_repository()
        item1 = ItemEstoque(produto_id="123", quantidade=10)
        item2 = ItemEstoque(produto_id="456", quantidade=5)

        repo.salvar(item1)
        repo.salvar(item2)
        repo.limpar_estoque()
        resultado = repo.obter_todos_itens()

        assert len(resultado) == 0
