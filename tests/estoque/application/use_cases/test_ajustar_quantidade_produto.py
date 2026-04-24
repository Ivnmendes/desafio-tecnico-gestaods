from unittest import TestCase
from unittest.mock import Mock

from src.estoque.application.use_cases.ajustar_quantidade_produto import (
    ajustar_quantidade_produto,
)
from src.estoque.domain.exceptions import ProdutoIndisponivelError


class TestAjustarQuantidadeProduto(TestCase):

    def test_deve_ajustar_quantidade_quando_item_existe(self):

        repositorio = Mock()
        item = Mock()
        repositorio.obter_item_estoque.return_value = item

        ajustar_quantidade_produto(repositorio, "produto-1", 4)

        item.ajustar_quantidade.assert_called_once_with(4)

    def test_deve_lancar_erro_quando_item_nao_existe(self):

        repositorio = Mock()
        repositorio.obter_item_estoque.return_value = None

        with self.assertRaises(ProdutoIndisponivelError) as context:
            ajustar_quantidade_produto(repositorio, "produto-inexistente", 2)

        self.assertTrue("Produto não encontrado no estoque!" in str(context.exception))
