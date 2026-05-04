from unittest import TestCase

from produto.infrastructure.repositories.MemoryProdutoRepository import (
    MemoryProdutoRepository,
)
from tests.produto.domain.contract_tests import ProdutoRepositoryContract


class TestMemoryProdutoRepository(TestCase, ProdutoRepositoryContract):

    def create_repository(self):
        return MemoryProdutoRepository()
