from unittest import TestCase

from src.estoque.infrastructure.MemoryEstoqueRepository import MemoryEstoqueRepository
from tests.estoque.domain.contract_tests import EstoqueRepositoryContract


class TestMemoryEstoqueRepository(TestCase, EstoqueRepositoryContract):

    def create_repository(self):
        return MemoryEstoqueRepository()
