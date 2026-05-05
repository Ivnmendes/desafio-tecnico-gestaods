from unittest import TestCase

import pytest

from estoque.infrastructure.django.repositories.DjangoEstoqueRepository import (
    DjangoEstoqueRepository,
)
from produto.domain.entities import Produto
from produto.infrastructure.django.repositories.DjangoProdutoRepository import (
    DjangoProdutoRepository,
)
from tests.estoque.domain.contract_tests import EstoqueRepositoryContract


@pytest.mark.django_db
class TestDjangoEstoqueRepository(TestCase, EstoqueRepositoryContract):

    def create_repository(self):
        return DjangoEstoqueRepository()

    def setup_produto(self, produto: Produto):
        produto_repo = DjangoProdutoRepository()
        produto_repo.salvar(produto)
