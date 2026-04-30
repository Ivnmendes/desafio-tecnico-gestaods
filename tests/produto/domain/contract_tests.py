from abc import ABC, abstractmethod

from estoque.domain.exceptions import ProdutoIndisponivelError
from src.produto.domain.entities import Produto


class ProdutoRepositoryContract(ABC):

    @abstractmethod
    def create_repository(self):
        """Método factory que deve ser sobrescrito."""
        pass

    def test_deve_salvar_e_recuperar_produto(self):

        repo = self.create_repository()
        produto = Produto(id="123", nome="Produto A", preco=10.0)

        repo.salvar(produto)
        resultado = repo.obter_por_id("123")

        assert resultado.nome == "Produto A"
        assert resultado.preco == 10.0

    def test_deve_remover_produto(self):

        repo = self.create_repository()
        produto = Produto(id="123", nome="Produto A", preco=10.0)

        repo.salvar(produto)
        repo.remover("123")
        resultado = repo.obter_por_id("123")

        assert resultado is None

    def test_deve_obter_todos_produtos(self):

        repo = self.create_repository()
        produto1 = Produto(id="123", nome="Produto A", preco=10.0)
        produto2 = Produto(id="456", nome="Produto B", preco=20.0)

        repo.salvar(produto1)
        repo.salvar(produto2)
        resultado = repo.obter_todos_produtos()

        assert len(resultado) == 2

    def test_deve_lancar_erro_ao_obter_produto_inexistente(self):

        repo = self.create_repository()

        excecao_lancada = False
        try:
            repo.obter_item_estoque("inexistente")
        except ProdutoIndisponivelError:
            excecao_lancada = True

        assert excecao_lancada is True, "Deveria ter lançado ProdutoIndisponivelError"
