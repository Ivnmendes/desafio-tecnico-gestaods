from unittest import TestCase

import pytest

from produto.infrastructure.django.repositories.DjangoProdutoRepository import (
    DjangoProdutoRepository,
)
from tests.produto.domain.contract_tests import ProdutoRepositoryContract


@pytest.mark.django_db
class TestDjangoProdutoRepository(TestCase, ProdutoRepositoryContract):

    def create_repository(self):
        return DjangoProdutoRepository()
