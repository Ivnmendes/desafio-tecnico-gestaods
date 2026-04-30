from unittest import TestCase

from src.produto.infrastructure.MemoryProdutoRepository import MemoryProdutoRepository
from tests.produto.domain.contract_tests import ProdutoRepositoryContract


class TestMemoryProdutoRepository(TestCase, ProdutoRepositoryContract):

    def create_repository(self):
        return MemoryProdutoRepository()
