from unittest import TestCase

from src.estoque.domain.value_objects import Quantidade


class TestQuantidade(TestCase):

    def test_nao_deve_permitir_quantidade_inicial_negativa(self):
        with self.assertRaises(ValueError) as context:
            Quantidade(-1)

        self.assertTrue("O estoque não pode ser negativo!" in str(context.exception))

    def test_deve_somar_quantidade_positiva(self):
        quantidade = Quantidade(2)

        quantidade_atualizada = quantidade.somar(3)

        self.assertEqual(5, quantidade_atualizada.valor)

    def test_nao_deve_permitir_resultado_negativo_na_soma(self):
        quantidade = Quantidade(2)

        with self.assertRaises(ValueError) as context:
            quantidade.somar(-3)

        self.assertTrue("O estoque não pode ser negativo!" in str(context.exception))
