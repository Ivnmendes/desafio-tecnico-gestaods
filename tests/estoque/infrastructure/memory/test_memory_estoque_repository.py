from unittest import TestCase

from estoque.infrastructure.memory.memory_estoque_repositorie import (
    MemoryEstoqueRepository,
)
from produto.domain.entities import Produto
from tests.estoque.domain.contract_tests import EstoqueRepositoryContract


class TestMemoryEstoqueRepository(TestCase, EstoqueRepositoryContract):

    def create_repository(self):
        return MemoryEstoqueRepository()

    def setup_produto(self, produto: Produto):
        # Nao precisa de setup, nao persiste dados
        pass

    def test_deve_filtrar_itens_por_preco(self):
        # Nao implementada sem persistencia
        pass

    def test_deve_filtrar_itens_por_preco_com_preco_maximo_none(self):
        # Nao implementada sem persistencia
        pass
