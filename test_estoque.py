

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
    produto4 = Produto(
        nome = "Caderno",
        valor = 20
    )

    def test_deve_permitir_criar_estoque_vazio(self):

        estoque = Estoque()
        self.assertEqual({}, estoque.disponivel)

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

    def test_somar_valor_estoque(self):

        lista_produtos = [
            {self.produto1: 1},
            {self.produto2: 0},
            {self.produto3: 4}
        ]
        estoque = Estoque(lista_produtos)
        self.assertEqual(20.7, estoque.total_valor_estoque())

    def test_somar_estoque_vazio(self):

        estoque = Estoque()
        self.assertEqual(0, estoque.total_valor_estoque())

    def test_total_produtos_estoque(self):

        lista_produtos = [
            {self.produto1: 1},
            {self.produto2: 0},
            {self.produto3: 4}
        ]
        estoque = Estoque(lista_produtos)
        self.assertEqual(5, estoque.total_produtos_estoque())

    def test_total_produtos_estoque_vazio(self):

        estoque = Estoque()
        self.assertEqual(0, estoque.total_produtos_estoque())

    def test_ajustar_quantidade_produto_estoque_adicionar(self):

        lista_produtos = [
            {self.produto1: 1},
            {self.produto2: 0},
            {self.produto3: 4}
        ]
        estoque = Estoque(lista_produtos)

        estoque.ajustar_quantidade_produto(self.produto1, 1)
        self.assertEqual(2, estoque.disponivel[self.produto1])

    def test_ajustar_quantidade_produto_estoque_produto_nao_existe(self):
        lista_produtos = [
            {self.produto1: 1},
            {self.produto2: 0},
            {self.produto3: 4}
        ]
        estoque = Estoque(lista_produtos)

        with self.assertRaises(Exception) as context:
            estoque.ajustar_quantidade_produto(self.produto4, 1)
        self.assertTrue("Produto não disponível no estoque!" in str(context.exception))

    def test_ajustar_quantidade_produto_estoque_remover(self):
        
        lista_produtos = [
            {self.produto1: 1},
            {self.produto2: 0},
            {self.produto3: 4}
        ]
        estoque = Estoque(lista_produtos)

        estoque.ajustar_quantidade_produto(self.produto1, -1)
        self.assertEqual(0, estoque.disponivel[self.produto1])

    def test_nao_deve_ajustar_estoque_quando_resultado_negativo(self):
        
        lista_produtos = [
            {self.produto1: 1},
            {self.produto2: 0},
            {self.produto3: 4}
        ]
        estoque = Estoque(lista_produtos)

        with self.assertRaises(Exception) as context:
            estoque.ajustar_quantidade_produto(self.produto1, -2)
        self.assertTrue("O estoque atualizado do produto não pode ser negativo!" in str(context.exception))

    def test_adicionar_produto_nao_existente_estoque(self):

        lista_produtos = [
            {self.produto1: 1},
            {self.produto2: 0},
            {self.produto3: 4}
        ]
        estoque = Estoque(lista_produtos)

        estoque.adicionar_produto(self.produto4, 3)
        self.assertTrue(self.produto4 in estoque.disponivel)

    def test_adicionar_produto_estoque_quantidade_negativa(self):

        lista_produtos = [
            {self.produto1: 1},
            {self.produto2: 0},
            {self.produto3: 4}
        ]
        estoque = Estoque(lista_produtos)

        with self.assertRaises(Exception) as context:
            estoque.adicionar_produto(self.produto4, -3)
        self.assertTrue("O estoque do produto não pode ser negativo!" in str(context.exception))

    def test_adicionar_produto_existente_estoque(self):

        lista_produtos = [
            {self.produto1: 1},
            {self.produto2: 0},
            {self.produto3: 4}
        ]
        estoque = Estoque(lista_produtos)

        estoque.adicionar_produto(self.produto3, 3)
        self.assertEqual(7, estoque.disponivel[self.produto3])

    def test_remover_produto_existente_estoque(self):

        lista_produtos = [
            {self.produto1: 1},
            {self.produto2: 0},
            {self.produto3: 4}
        ]
        estoque = Estoque(lista_produtos)

        estoque.remover_produto(self.produto3)
        self.assertTrue(self.produto3 not in estoque.disponivel)

    def test_remover_produto_nao_existente_estoque(self):

        lista_produtos = [
            {self.produto1: 1},
            {self.produto2: 0},
            {self.produto3: 4}
        ]
        estoque = Estoque(lista_produtos)

        with self.assertRaises(Exception) as context:
            estoque.remover_produto(self.produto4)
        self.assertTrue("Produto não encontrado no estoque!" in str(context.exception))

    def test_verificar_estoque_produto_existe(self):

        lista_produtos = [
            {self.produto1: 1},
            {self.produto2: 0},
            {self.produto3: 4}
        ]
        estoque = Estoque(lista_produtos)

        dados = estoque.verificar_estoque_produto(self.produto2)
        self.assertEqual({ "nome": "Lápis", "valor_individual": 1.2, "quantidade": 0 }, dados)

    def test_verificar_estoque_produto_inexiste(self):

        lista_produtos = [
            {self.produto1: 1},
            {self.produto2: 0},
            {self.produto3: 4}
        ]
        estoque = Estoque(lista_produtos)

        with self.assertRaises(Exception) as context:
            estoque.verificar_estoque_produto(self.produto4)
        self.assertTrue("Produto não encontrado no estoque!" in str(context.exception))

    def test_limpar_estoque(self):

        lista_produtos = [
            {self.produto1: 1},
            {self.produto2: 0},
            {self.produto3: 4}
        ]
        estoque = Estoque(lista_produtos)

        estoque.limpar_estoque()
        self.assertEqual({}, estoque.disponivel)

    def test_adicionar_produto_pos_estoque_limpo(self):

        lista_produtos = [
            {self.produto1: 1},
            {self.produto2: 0},
            {self.produto3: 4}
        ]
        estoque = Estoque(lista_produtos)

        estoque.limpar_estoque()
        estoque.adicionar_produto(self.produto4, 1)
        self.assertTrue(self.produto4 in estoque.disponivel)

    def test_listar_produtos_estoque(self):

        lista_produtos = [
            {self.produto1: 1},
            {self.produto2: 0},
            {self.produto3: 4}
        ]
        estoque = Estoque(lista_produtos)

        lista_produtos_retorno = estoque.listar_produtos_estoque()
        self.assertEqual(lista_produtos_retorno, [self.produto1, self.produto2, self.produto3])

    def test_listar_produtos_estoque_vazio(self):

        estoque = Estoque()

        lista_produtos_retorno = estoque.listar_produtos_estoque()
        self.assertEqual(lista_produtos_retorno, [])

    def test_listar_produtos_estoque_filtro_preco(self):

        lista_produtos = [
            {self.produto1: 1},
            {self.produto2: 0},
            {self.produto3: 4},
            {self.produto4: 10}
        ]
        estoque = Estoque(lista_produtos)

        lista_produtos_retorno = estoque.listar_produtos_estoque(min_valor = 3.4, max_valor = 10)
        self.assertEqual(lista_produtos_retorno, [self.produto1, self.produto3])

    def test_listar_produtos_estoque_filtro_preco_filtros_invalidos(self):

        lista_produtos = [
            {self.produto1: 1},
            {self.produto2: 0},
            {self.produto3: 4},
            {self.produto4: 10}
        ]
        estoque = Estoque(lista_produtos)

        with self.assertRaises(Exception) as context:
            estoque.listar_produtos_estoque(min_valor = 3.6, max_valor = 2)
        self.assertTrue("Filtros inválidos" in str(context.exception))