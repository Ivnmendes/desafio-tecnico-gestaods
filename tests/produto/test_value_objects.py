
from unittest import TestCase

from src.produto.domain.value_objects import NomeProduto, Preco

class TestNomeProduto(TestCase):

    def test_nao_deve_permitir_nome_vazio(self):
        
        with self.assertRaises(ValueError) as context:
            NomeProduto("")
        self.assertTrue("Não é possível iniciar um produto com nome vazio!" in str(context.exception))

    def test_criar_nome_produto(self):

        nome_produto = NomeProduto("Nome")
        self.assertEqual("Nome", nome_produto.valor)


class TestPreco(TestCase):

    def test_nao_deve_permitir_valor_negativo(self):

        with self.assertRaises(ValueError) as context:
            Preco(-2.1)
        self.assertTrue("O valor não pode ser zerado/negativo!" in str(context.exception))

    def test_criar_preco(self):

        preco = Preco(3.2)
        self.assertEqual(3.2, preco.valor)