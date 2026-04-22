
from unittest import TestCase

from src.produto.domain.entities import Produto
from src.produto.domain.value_objects import NomeProduto, Preco

class TestProduto(TestCase):

    def test_nao_deve_permitir_criar_produto_sem_nome(self):

        with self.assertRaises(ValueError) as context:
            Produto(
                nome = "",
                preco = 3.2,
            )
        self.assertTrue("Não é possível iniciar um produto com nome vazio!" in str(context.exception))

    def test_nao_deve_criar_produto_com_valor_zerado(self):

        with self.assertRaises(ValueError) as context:
            Produto(
                nome = "Garrafa",
                preco = 0,
            )
        self.assertTrue("O valor não pode ser zerado/negativo!" in str(context.exception))

    def test_nao_deve_criar_produto_com_valor_negativo(self):

        with self.assertRaises(ValueError) as context:
            Produto(
                nome = "Garrafa",
                preco = -1,
            )
        self.assertTrue("O valor não pode ser zerado/negativo!" in str(context.exception))

    def test_deve_permitir_alterar_valor_produto(self):

        produto = Produto(
            nome = "Garrafa",
            preco = 2.1
        )

        produto.alterar_preco(2.3)
        self.assertEqual(2.3, produto.preco.valor)