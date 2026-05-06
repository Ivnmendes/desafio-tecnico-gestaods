from unittest import TestCase
from unittest.mock import Mock

from estoque.application.use_cases.adicionar_produto_ao_estoque import (
    AdicionarProdutoAoEstoqueUseCase,
)


class TestAdicionarProdutoAoEstoque(TestCase):

    def test_deve_ajustar_item_quando_produto_ja_existe(self):

        repositorio_estoque = Mock()
        repositorio_produto = Mock()
        item = Mock()
        produto = Mock()
        repositorio_estoque.obter_item_estoque.return_value = item
        repositorio_produto.obter_produto.return_value = produto

        AdicionarProdutoAoEstoqueUseCase(
            repositorio_estoque, repositorio_produto, "produto-1", 3
        )

        item.ajustar_quantidade.assert_called_once_with(3)
        repositorio_estoque.salvar.assert_called_once_with(item)

    def test_deve_criar_item_quando_produto_nao_existe_no_estoque(self):

        repositorio_estoque = Mock()
        repositorio_produto = Mock()
        repositorio_estoque.obter_item_estoque.return_value = None
        repositorio_produto.obter_produto.return_value = Mock()

        AdicionarProdutoAoEstoqueUseCase(
            repositorio_estoque, repositorio_produto, "produto-1", 3
        )

        repositorio_estoque.salvar.assert_called_once()

    def test_deve_lancar_erro_quando_produto_nao_existe(self):

        repositorio_estoque = Mock()
        repositorio_produto = Mock()
        repositorio_estoque.obter_item_estoque.return_value = None
        repositorio_produto.obter_produto.return_value = None

        with self.assertRaises(Exception):
            AdicionarProdutoAoEstoqueUseCase(
                repositorio_estoque, repositorio_produto, "produto-1", 3
            )
