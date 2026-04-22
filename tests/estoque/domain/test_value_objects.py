
from unittest import TestCase

from src.estoque.domain.value_objects import Quantidade

class TestQuantidade(TestCase):

    def test_nao_deve_permitir_quantidade_negativa(self):
        
        with self.assertRaises(ValueError) as context:
            Quantidade(-1)
        self.assertTrue("O estoque não pode ser negativo!" in str(context.exception))