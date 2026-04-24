from unittest import TestCase

from src.estoque.domain.entities import ItemEstoque


class TestItemEstoque(TestCase):

    def test_deve_criar_item_estoque(self):

        item = ItemEstoque(produto_id="produto-1", quantidade=3)

        self.assertEqual("produto-1", item.produto_id)
        self.assertEqual(3, item.quantidade.valor)

    def test_deve_ajustar_quantidade_item_estoque(self):

        item = ItemEstoque(produto_id="produto-1", quantidade=3)

        item.ajustar_quantidade(2)

        self.assertEqual(5, item.quantidade.valor)
