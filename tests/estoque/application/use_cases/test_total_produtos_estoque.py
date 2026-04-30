from unittest import TestCase
from unittest.mock import Mock

from estoque.application.use_cases.total_produtos_estoque import total_produtos_estoque
from estoque.domain.entities import ItemEstoque


class TestTotalProdutosEstoque(TestCase):

    def test_deve_somar_total_de_unidades_no_estoque(self):

        repositorio = Mock()

        item1 = ItemEstoque("produto-1", 2)
        item2 = ItemEstoque("produto-2", 1)

        repositorio.obter_todos_itens_estoque.return_value = [item1, item2]

        total = total_produtos_estoque(repositorio)

        self.assertEqual(3, total)
        repositorio.obter_todos_itens_estoque.assert_called_once_with()
