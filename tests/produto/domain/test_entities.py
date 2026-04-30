from unittest import TestCase

from produto.domain.entities import Produto


class TestProduto(TestCase):

    def test_nao_deve_permitir_criar_produto_sem_nome(self):

        with self.assertRaises(ValueError) as context:
            Produto(
                nome="",
                preco=3.2,
            )
        self.assertTrue(
            "Não é possível iniciar um produto com nome vazio!"
            in str(context.exception)
        )

    def test_nao_deve_criar_produto_com_valor_zerado(self):

        with self.assertRaises(ValueError) as context:
            Produto(
                nome="Garrafa",
                preco=0,
            )
        self.assertTrue(
            "O valor não pode ser zerado/negativo!" in str(context.exception)
        )

    def test_nao_deve_criar_produto_com_valor_negativo(self):

        with self.assertRaises(ValueError) as context:
            Produto(
                nome="Garrafa",
                preco=-1,
            )
        self.assertTrue(
            "O valor não pode ser zerado/negativo!" in str(context.exception)
        )

    def test_deve_permitir_alterar_valor_produto(self):

        produto = Produto(nome="Garrafa", preco=2.1)

        produto.alterar_preco(2.3)
        self.assertEqual(2.3, produto.preco)

    def test_nao_deve_permitir_alterar_valor_produto_para_valor_positivo(self):

        produto = Produto(nome="Garrafa", preco=2.1)

        with self.assertRaises(ValueError) as context:
            produto.alterar_preco(-1)
        self.assertTrue(
            "O valor não pode ser zerado/negativo!" in str(context.exception)
        )

    def test_nao_deve_permitir_alterar_valor_produto_para_valor_zerado(self):

        produto = Produto(nome="Garrafa", preco=2.1)

        with self.assertRaises(ValueError) as context:
            produto.alterar_preco(0)
        self.assertTrue(
            "O valor não pode ser zerado/negativo!" in str(context.exception)
        )

    def test_deve_gerar_id_automaticamente(self):

        produto = Produto(nome="Garrafa", preco=2.1)

        self.assertIsNotNone(produto.id)

    def test_deve_aceitar_id_passado_no_construtor(self):

        produto = Produto(nome="Garrafa", preco=2.1, id="123")

        self.assertEqual("123", produto.id)

    def test_representacao_string(self):

        produto = Produto(nome="Garrafa", preco=2.1)

        self.assertEqual("Garrafa - R$2.1", str(produto))
        self.assertEqual(
            f"Produto(id={produto.id}, nome=Garrafa, preco=2.1)", repr(produto)
        )
