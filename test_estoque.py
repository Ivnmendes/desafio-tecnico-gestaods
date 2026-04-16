

from unittest import TestCase
from estoque import Estoque
from produto import Produto

class TestEstoque(TestCase):

    produto1 = Produto(
        nome = "Garrafa",
        valor = 3.5
    )
    produto2 = Produto(
        nome = "Lápis",
        valor = 1.2
    )
    produto3 = Produto(
        nome = "Borracha",
        valor = 4.3
    )

    def test_deve_permitir_criar_estoque_vazio(self):

        estoque = Estoque()
        self.assertEqual([], estoque.disponivel)

    def test_deve_permitir_multiplos_itens_estoque(self):

        lista_produtos = [
            {self.produto1: 1},
            {self.produto2: 2},
            {self.produto3: 4}
        ]
        estoque = Estoque(lista_produtos)
        self.assertEqual(3, len(estoque.disponivel))

    def test_deve_permitir_estoque_zerado_de_produto(self):

        lista_produtos = [
            {self.produto1: 1},
            {self.produto2: 0},
            {self.produto3: 4}
        ]
        estoque = Estoque(lista_produtos)
        self.assertEqual(3, len(estoque.disponivel))

    def test_nao_deve_permitir_estoque_negativo_de_produto(self):

        lista_produtos = [
            {self.produto1: 1},
            {self.produto2: -1},
            {self.produto3: 4}
        ]
        
        with self.assertRaises(Exception) as context:
            Estoque(lista_produtos)
        self.assertTrue("O estoque de nenhum produto pode ser negativo!" in str(context.exception))