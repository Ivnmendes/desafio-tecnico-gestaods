from unittest import TestCase

from produto.infrastructure.memory.memory_produto_repositorie import (
    MemoryProdutoRepository,
)
from tests.produto.domain.contract_tests import ProdutoRepositoryContract


class TestMemoryProdutoRepository(TestCase, ProdutoRepositoryContract):

    def create_repository(self):
        return MemoryProdutoRepository()
