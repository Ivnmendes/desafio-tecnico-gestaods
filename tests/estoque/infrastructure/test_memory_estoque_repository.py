from unittest import TestCase

from estoque.infrastructure.MemoryEstoqueRepository import MemoryEstoqueRepository
from tests.estoque.domain.contract_tests import EstoqueRepositoryContract


class TestMemoryEstoqueRepository(TestCase, EstoqueRepositoryContract):

    def create_repository(self):
        return MemoryEstoqueRepository()

    def setup_produto(self, id: str, nome: str, preco: float):
        # Nao precisa de setup, nao persiste dados
        pass
