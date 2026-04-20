
from unittest import TestCase

from produto.domain.entities import Produto
from produto.domain.value_objects import NomeProduto, Preco

class TestProduto(TestCase):

    def test_nao_deve_permitir_criar_produto_sem_nome(self):

        with self.assertRaises(ValueError) as context:
            Produto(
                nome = NomeProduto(""),
                preco = Preco(3.2),
            )
        self.assertTrue("Não é possível iniciar um produto com nome vazio!" in str(context.exception))

    def test_nao_deve_criar_produto_com_valor_zerado(self):

        with self.assertRaises(ValueError) as context:
            Produto(
                nome = NomeProduto("Garrafa"),
                preco = Preco(0),
            )
        self.assertTrue("O valor não pode ser zerado/negativo!" in str(context.exception))

    def test_nao_deve_criar_produto_com_valor_negativo(self):

        with self.assertRaises(ValueError) as context:
            Produto(
                nome = NomeProduto("Garrafa"),
                preco = Preco(-1),
            )
        self.assertTrue("O valor não pode ser zerado/negativo!" in str(context.exception))

    def test_deve_permitir_alterar_valor_produto(self):

        produto = Produto(
            nome = NomeProduto("Garrafa"),
            preco = Preco(2.1)
        )

        produto.alterar_preco(Preco(2.3))
        self.assertEqual(2.3, produto.preco.valor)

    def test_nao_deve_permitir_alterar_valor_negativo_produto(self):

        produto = Produto(
            nome = NomeProduto("Garrafa"),
            preco = Preco(2.1)
        )
        with self.assertRaises(ValueError) as context:
            produto.alterar_preco(Preco(-2.3))
        self.assertTrue("O valor não pode ser zerado/negativo!" in str(context.exception))

    def test_nao_deve_permitir_alterar_valor_zerado_produto(self):

        produto = Produto(
            nome = NomeProduto("Garrafa"),
            preco = Preco(2.1)
        )
        with self.assertRaises(ValueError) as context:
            produto.alterar_preco(Preco(0))
        self.assertTrue("O valor não pode ser zerado/negativo!" in str(context.exception))