from unittest import TestCase
from unittest.mock import Mock

from estoque.application.use_cases.filtrar_estoque_por_preco import (
    filtrar_estoque_por_preco,
)


class TestFiltrarEstoquePorPreco(TestCase):

    def test_deve_filtrar_produtos_por_preco(self):

        repositorio = Mock()
        repositorio.filtrar_produtos_preco.return_value = ["produto-1", "produto-2"]

        resultado = filtrar_estoque_por_preco(
            repositorio, preco_minimo=10.0, preco_maximo=50.0
        )

        repositorio.filtrar_produtos_preco.assert_called_once_with(10.0, 50.0)
        self.assertEqual(resultado, ["produto-1", "produto-2"])

    def test_deve_lancar_erro_quando_preco_minimo_negativo(self):

        repositorio = Mock()

        with self.assertRaises(ValueError) as context:
            filtrar_estoque_por_preco(repositorio, preco_minimo=-5.0)

        self.assertTrue(
            "O preço mínimo não pode ser negativo." in str(context.exception)
        )

    def test_deve_lancar_erro_quando_preco_maximo_negativo(self):

        repositorio = Mock()

        with self.assertRaises(ValueError) as context:
            filtrar_estoque_por_preco(repositorio, preco_maximo=-10.0)

        self.assertTrue(
            "O preço máximo não pode ser negativo." in str(context.exception)
        )

    def test_deve_lancar_erro_quando_preco_minimo_maior_que_maximo(self):

        repositorio = Mock()

        with self.assertRaises(ValueError) as context:
            filtrar_estoque_por_preco(repositorio, preco_minimo=60.0, preco_maximo=50.0)

        self.assertTrue(
            "O preço mínimo não pode ser maior que o preço máximo."
            in str(context.exception)
        )
