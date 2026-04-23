from unittest import TestCase
from unittest.mock import Mock

from src.estoque.application.use_cases.adicionar_produto_ao_estoque import (
    adicionar_produto_ao_estoque,
)


class TestAdicionarProdutoAoEstoque(TestCase):

    def test_deve_ajustar_item_quando_produto_ja_existe(self):

        repositorio = Mock()
        item = Mock()
        repositorio.obter_item_estoque.return_value = item

        adicionar_produto_ao_estoque(repositorio, "produto-1", 3)

        item.ajustar_quantidade.assert_called_once_with(3)
        repositorio.salvar.assert_called_once_with(item)

    def test_deve_criar_item_quando_produto_nao_existe(self):

        repositorio = Mock()
        repositorio.obter_item_estoque.return_value = None

        adicionar_produto_ao_estoque(repositorio, "produto-1", 3)

        repositorio.salvar.assert_called_once()
