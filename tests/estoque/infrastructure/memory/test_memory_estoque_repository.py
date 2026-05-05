from unittest import TestCase

from estoque.infrastructure.memory.MemoryEstoqueRepository import (
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
