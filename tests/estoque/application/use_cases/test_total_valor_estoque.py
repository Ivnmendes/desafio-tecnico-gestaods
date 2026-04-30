from unittest import TestCase
from unittest.mock import Mock

from estoque.application.use_cases.total_valor_estoque import total_valor_estoque
from estoque.domain.entities import ItemEstoque
from produto.domain.entities import Produto


class TestTotalValorEstoque(TestCase):

    def test_deve_somar_valor_total_do_estoque(self):

        repositorio_estoque = Mock()
        repositorio_produto = Mock()

        item1 = ItemEstoque("produto-1", 2)
        item2 = ItemEstoque("produto-2", 1)

        produto1 = Produto(id="produto-1", nome="Produto 1", preco=10.0)
        produto2 = Produto(id="produto-2", nome="Produto 2", preco=4.0)

        repositorio_estoque.obter_todos_itens_estoque.return_value = [item1, item2]
        repositorio_produto.buscar_por_ids.return_value = [produto1, produto2]

        total = total_valor_estoque(repositorio_estoque, repositorio_produto)

        self.assertEqual(24.0, total)
        repositorio_estoque.obter_todos_itens_estoque.assert_called_once_with()

    def test_deve_somar_valor_total_do_estoque_vazio(self):

        repositorio_estoque = Mock()
        repositorio_produto = Mock()

        repositorio_estoque.obter_todos_itens_estoque.return_value = []
        repositorio_produto.buscar_por_ids.return_value = []

        total = total_valor_estoque(repositorio_estoque, repositorio_produto)

        self.assertEqual(0.0, total)
        repositorio_estoque.obter_todos_itens_estoque.assert_called_once_with()
