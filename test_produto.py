
from unittest import TestCase
from produto import Produto

class TestProduto(TestCase):

    def test_nao_deve_permitir_criar_produto_sem_nome(self):

        with self.assertRaises(Exception) as context:
            Produto(
                nome = "",
                valor = 3.2,
            )
        self.assertTrue("Não é possível iniciar um produto com nome vazio!" in str(context.exception))

    def test_nao_deve_criar_produto_com_valor_zerado(self):

        with self.assertRaises(Exception) as context:
            Produto(
                nome = "Garrafa",
                valor = 0,
            )
        self.assertTrue("Não é possível iniciar um produto com valor zerado/negativo!" in str(context.exception))

    def test_nao_deve_criar_produto_com_valor_negativo(self):

        with self.assertRaises(Exception) as context:
            Produto(
                nome = "Garrafa",
                valor = -1,
            )
        self.assertTrue("Não é possível iniciar um produto com valor zerado/negativo!" in str(context.exception))

    def test_deve_permitir_alterar_valor_produto(self):

        produto = Produto(
            nome = "Garrafa",
            valor = 2.1
        )
        produto.alterar_valor(2.3)
        self.assertEqual(2.3, produto.valor)

    def test_nao_deve_permitir_alterar_valor_negativo_produto(self):

        produto = Produto(
            nome = "Garrafa",
            valor = 2.1
        )
        with self.assertRaises(Exception) as context:
            produto.alterar_valor(-2.3)
        self.assertTrue("O valor não pode ser zerado/negativo!" in str(context.exception))

    def test_nao_deve_permitir_alterar_valor_zerado_produto(self):

        produto = Produto(
            nome = "Garrafa",
            valor = 2.1
        )
        with self.assertRaises(Exception) as context:
            produto.alterar_valor(0)
        self.assertTrue("O valor não pode ser zerado/negativo!" in str(context.exception))