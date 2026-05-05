from unittest import TestCase

from estoque.domain.entities import ItemEstoque
from produto.domain.entities import Produto


class TestItemEstoque(TestCase):

    def test_deve_criar_item_estoque(self):

        item = ItemEstoque(
            Produto(id="produto-1", nome="Produto 1", preco=10.0), quantidade=3
        )

        self.assertEqual("produto-1", item.produto.id)
        self.assertEqual(3, item.quantidade)

    def test_deve_ajustar_quantidade_item_estoque(self):

        item = ItemEstoque(
            Produto(id="produto-1", nome="Produto 1", preco=10.0), quantidade=3
        )

        item.ajustar_quantidade(2)

        self.assertEqual(5, item.quantidade)

    def test_deve_representar_item_estoque_com_str(self):

        item = ItemEstoque(
            Produto(id="produto-1", nome="Produto 1", preco=10.0), quantidade=3
        )

        self.assertEqual(
            "ItemEstoque(produto=Produto(id='produto-1', "
            "nome='Produto 1', preco=10.0), "
            "quantidade=3"
            ")",
            repr(item),
        )
