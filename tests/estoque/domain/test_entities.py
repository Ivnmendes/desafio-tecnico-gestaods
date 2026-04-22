
from unittest import TestCase

from src.estoque.domain.entities import Estoque, ItemEstoque
from src.estoque.domain.exceptions import ProdutoIndisponivelError

from src.produto.domain.entities import Produto

class TestEstoque(TestCase):

    produto1 = Produto(
        nome = "Garrafa",
        preco = 3.5
    )
    produto2 = Produto(
        nome = "Lápis",
        preco = 1.2
    )
    produto3 = Produto(
        nome = "Borracha",
        preco = 4.3
    )
    produto4 = Produto(
        nome = "Caderno",
        preco = 20
    )

    def test_deve_permitir_criar_estoque_vazio(self):

        estoque = Estoque()
        self.assertEqual({}, estoque.itens)

    def test_deve_permitir_multiplos_itens_estoque(self):

        item_estoque_1 = ItemEstoque(
            produto = self.produto1, 
            quantidade = 1
        )
        item_estoque_2 = ItemEstoque(
            produto = self.produto2, 
            quantidade = 2
        )
        item_estoque_3 = ItemEstoque(
            produto = self.produto3, 
            quantidade = 4
        )
        produtos = {
            self.produto1.id: item_estoque_1,
            self.produto2.id: item_estoque_2,
            self.produto3.id: item_estoque_3,
        }
        estoque = Estoque(produtos)

        self.assertEqual(3, len(estoque.itens))

    def test_somar_valor_estoque(self):

        item_estoque_1 = ItemEstoque(
            produto = self.produto1, 
            quantidade = 1
        )
        item_estoque_2 = ItemEstoque(
            produto = self.produto2, 
            quantidade = 0
        )
        item_estoque_3 = ItemEstoque(
            produto = self.produto3, 
            quantidade = 4
        )
        produtos = {
            self.produto1.id: item_estoque_1,
            self.produto2.id: item_estoque_2,
            self.produto3.id: item_estoque_3,
        }
        estoque = Estoque(produtos)

        self.assertEqual(20.7, estoque.total_valor_estoque())

    def test_somar_estoque_vazio(self):

        estoque = Estoque()
        self.assertEqual(0, estoque.total_valor_estoque())

    def test_total_produtos_estoque(self):

        item_estoque_1 = ItemEstoque(
            produto = self.produto1, 
            quantidade = 1
        )
        item_estoque_2 = ItemEstoque(
            produto = self.produto2, 
            quantidade = 0
        )
        item_estoque_3 = ItemEstoque(
            produto = self.produto3, 
            quantidade = 4
        )
        produtos = {
            self.produto1.id: item_estoque_1,
            self.produto2.id: item_estoque_2,
            self.produto3.id: item_estoque_3,
        }
        estoque = Estoque(produtos)
        
        self.assertEqual(5, estoque.total_produtos_estoque())

    def test_total_produtos_estoque_vazio(self):

        estoque = Estoque()
        self.assertEqual(0, estoque.total_produtos_estoque())

    def test_ajustar_quantidade_produto_estoque_adicionar(self):

        item_estoque_1 = ItemEstoque(
            produto = self.produto1, 
            quantidade = 1
        )
        item_estoque_2 = ItemEstoque(
            produto = self.produto2, 
            quantidade = 0
        )
        item_estoque_3 = ItemEstoque(
            produto = self.produto3, 
            quantidade = 4
        )
        produtos = {
            self.produto1.id: item_estoque_1,
            self.produto2.id: item_estoque_2,
            self.produto3.id: item_estoque_3,
        }
        estoque = Estoque(produtos)

        estoque.ajustar_quantidade_produto(self.produto1, 1)
        produto_estoque = estoque.itens[self.produto1.id]
        self.assertEqual(2, produto_estoque.quantidade.valor)

    def test_ajustar_quantidade_produto_estoque_produto_nao_existe(self):

        item_estoque_1 = ItemEstoque(
            produto = self.produto1, 
            quantidade = 1
        )
        item_estoque_2 = ItemEstoque(
            produto = self.produto2, 
            quantidade = 0
        )
        item_estoque_3 = ItemEstoque(
            produto = self.produto3, 
            quantidade = 4
        )
        produtos = {
            self.produto1.id: item_estoque_1,
            self.produto2.id: item_estoque_2,
            self.produto3.id: item_estoque_3,
        }
        estoque = Estoque(produtos)

        with self.assertRaises(ProdutoIndisponivelError) as context:
            estoque.ajustar_quantidade_produto(self.produto4, 1)
        self.assertTrue("Produto não disponível no estoque!" in str(context.exception))

    def test_ajustar_quantidade_produto_estoque_remover(self):
        
        item_estoque_1 = ItemEstoque(
            produto = self.produto1, 
            quantidade = 1
        )
        item_estoque_2 = ItemEstoque(
            produto = self.produto2, 
            quantidade = 0
        )
        item_estoque_3 = ItemEstoque(
            produto = self.produto3, 
            quantidade = 4
        )
        produtos = {
            self.produto1.id: item_estoque_1,
            self.produto2.id: item_estoque_2,
            self.produto3.id: item_estoque_3,
        }
        estoque = Estoque(produtos)

        estoque.ajustar_quantidade_produto(self.produto1, -1)
        produto_estoque = estoque.itens[self.produto1.id]
        self.assertEqual(0, produto_estoque.quantidade.valor)

    def test_nao_deve_ajustar_estoque_quando_resultado_negativo(self):
        
        item_estoque_1 = ItemEstoque(
            produto = self.produto1, 
            quantidade = 1
        )
        item_estoque_2 = ItemEstoque(
            produto = self.produto2, 
            quantidade = 0
        )
        item_estoque_3 = ItemEstoque(
            produto = self.produto3, 
            quantidade = 4
        )
        produtos = {
            self.produto1.id: item_estoque_1,
            self.produto2.id: item_estoque_2,
            self.produto3.id: item_estoque_3,
        }
        estoque = Estoque(produtos)

        with self.assertRaises(ValueError) as context:
            estoque.ajustar_quantidade_produto(self.produto1, -2)
        self.assertTrue("O estoque não pode ser negativo!" in str(context.exception))

    def test_adicionar_produto_nao_existente_estoque(self):

        item_estoque_1 = ItemEstoque(
            produto = self.produto1, 
            quantidade = 1
        )
        item_estoque_2 = ItemEstoque(
            produto = self.produto2, 
            quantidade = 0
        )
        item_estoque_3 = ItemEstoque(
            produto = self.produto3, 
            quantidade = 4
        )
        produtos = {
            self.produto1.id: item_estoque_1,
            self.produto2.id: item_estoque_2,
            self.produto3.id: item_estoque_3,
        }
        estoque = Estoque(produtos)

        estoque.adicionar_produto(self.produto4, 3)
        self.assertTrue(self.produto4.id in estoque.itens)

    def test_adicionar_produto_estoque_quantidade_negativa(self):

        item_estoque_1 = ItemEstoque(
            produto = self.produto1, 
            quantidade = 1
        )
        item_estoque_2 = ItemEstoque(
            produto = self.produto2, 
            quantidade = 0
        )
        item_estoque_3 = ItemEstoque(
            produto = self.produto3, 
            quantidade = 4
        )
        produtos = {
            self.produto1.id: item_estoque_1,
            self.produto2.id: item_estoque_2,
            self.produto3.id: item_estoque_3,
        }
        estoque = Estoque(produtos)

        with self.assertRaises(ValueError) as context:
            estoque.adicionar_produto(self.produto4, -3)
        self.assertTrue("O estoque não pode ser negativo!" in str(context.exception))

    def test_adicionar_produto_existente_estoque(self):

        item_estoque_1 = ItemEstoque(
            produto = self.produto1, 
            quantidade = 1
        )
        item_estoque_2 = ItemEstoque(
            produto = self.produto2, 
            quantidade = 0
        )
        item_estoque_3 = ItemEstoque(
            produto = self.produto3, 
            quantidade = 4
        )
        produtos = {
            self.produto1.id: item_estoque_1,
            self.produto2.id: item_estoque_2,
            self.produto3.id: item_estoque_3,
        }
        estoque = Estoque(produtos)

        estoque.adicionar_produto(self.produto3, 3)
        produto_estoque = estoque.itens[self.produto3.id]
        self.assertEqual(7, produto_estoque.quantidade.valor)

    def test_remover_produto_existente_estoque(self):

        item_estoque_1 = ItemEstoque(
            produto = self.produto1, 
            quantidade = 1
        )
        item_estoque_2 = ItemEstoque(
            produto = self.produto2, 
            quantidade = 0
        )
        item_estoque_3 = ItemEstoque(
            produto = self.produto3, 
            quantidade = 4
        )
        produtos = {
            self.produto1.id: item_estoque_1,
            self.produto2.id: item_estoque_2,
            self.produto3.id: item_estoque_3,
        }
        estoque = Estoque(produtos)

        estoque.remover_produto(self.produto3)
        self.assertTrue(self.produto3 not in estoque.itens)

    def test_remover_produto_nao_existente_estoque(self):

        item_estoque_1 = ItemEstoque(
            produto = self.produto1, 
            quantidade = 1
        )
        item_estoque_2 = ItemEstoque(
            produto = self.produto2, 
            quantidade = 0
        )
        item_estoque_3 = ItemEstoque(
            produto = self.produto3, 
            quantidade = 4
        )
        produtos = {
            self.produto1.id: item_estoque_1,
            self.produto2.id: item_estoque_2,
            self.produto3.id: item_estoque_3,
        }
        estoque = Estoque(produtos)

        with self.assertRaises(ProdutoIndisponivelError) as context:
            estoque.remover_produto(self.produto4)
        self.assertTrue("Produto não encontrado no estoque!" in str(context.exception))

    def test_verificar_estoque_produto_existe(self):

        item_estoque_1 = ItemEstoque(
            produto = self.produto1, 
            quantidade = 1
        )
        item_estoque_2 = ItemEstoque(
            produto = self.produto2, 
            quantidade = 0
        )
        item_estoque_3 = ItemEstoque(
            produto = self.produto3, 
            quantidade = 4
        )
        produtos = {
            self.produto1.id: item_estoque_1,
            self.produto2.id: item_estoque_2,
            self.produto3.id: item_estoque_3,
        }
        estoque = Estoque(produtos)

        dados = estoque.verificar_estoque_produto(self.produto2)
        self.assertEqual({ "nome": "Lápis", "valor_individual": 1.2, "quantidade": 0 }, dados)

    def test_verificar_estoque_produto_inexiste(self):

        item_estoque_1 = ItemEstoque(
            produto = self.produto1, 
            quantidade = 1
        )
        item_estoque_2 = ItemEstoque(
            produto = self.produto2, 
            quantidade = 0
        )
        item_estoque_3 = ItemEstoque(
            produto = self.produto3, 
            quantidade = 4
        )
        produtos = {
            self.produto1.id: item_estoque_1,
            self.produto2.id: item_estoque_2,
            self.produto3.id: item_estoque_3,
        }
        estoque = Estoque(produtos)

        with self.assertRaises(ProdutoIndisponivelError) as context:
            estoque.verificar_estoque_produto(self.produto4)
        self.assertTrue("Produto não encontrado no estoque!" in str(context.exception))

    def test_limpar_estoque(self):

        item_estoque_1 = ItemEstoque(
            produto = self.produto1, 
            quantidade = 1
        )
        item_estoque_2 = ItemEstoque(
            produto = self.produto2, 
            quantidade = 0
        )
        item_estoque_3 = ItemEstoque(
            produto = self.produto3, 
            quantidade = 4
        )
        produtos = {
            self.produto1.id: item_estoque_1,
            self.produto2.id: item_estoque_2,
            self.produto3.id: item_estoque_3,
        }
        estoque = Estoque(produtos)

        estoque.limpar_estoque()
        self.assertEqual({}, estoque.itens)

    def test_adicionar_produto_pos_estoque_limpo(self):

        item_estoque_1 = ItemEstoque(
            produto = self.produto1, 
            quantidade = 1
        )
        item_estoque_2 = ItemEstoque(
            produto = self.produto2, 
            quantidade = 0
        )
        item_estoque_3 = ItemEstoque(
            produto = self.produto3, 
            quantidade = 4
        )
        produtos = {
            self.produto1.id: item_estoque_1,
            self.produto2.id: item_estoque_2,
            self.produto3.id: item_estoque_3,
        }
        estoque = Estoque(produtos)

        estoque.limpar_estoque()
        estoque.adicionar_produto(self.produto4, 1)
        self.assertTrue(self.produto4.id in estoque.itens)

    def test_listar_produtos_estoque(self):

        item_estoque_1 = ItemEstoque(
            produto = self.produto1, 
            quantidade = 1
        )
        item_estoque_2 = ItemEstoque(
            produto = self.produto2, 
            quantidade = 0
        )
        item_estoque_3 = ItemEstoque(
            produto = self.produto3, 
            quantidade = 4
        )
        produtos = {
            self.produto1.id: item_estoque_1,
            self.produto2.id: item_estoque_2,
            self.produto3.id: item_estoque_3,
        }
        estoque = Estoque(produtos)

        lista_produtos_retorno = estoque.listar_produtos_estoque()
        self.assertEqual(lista_produtos_retorno, [self.produto1, self.produto2, self.produto3])

    def test_listar_produtos_estoque_vazio(self):

        estoque = Estoque()

        lista_produtos_retorno = estoque.listar_produtos_estoque()
        self.assertEqual(lista_produtos_retorno, [])

    def test_listar_produtos_estoque_filtro_preco(self):
        
        item_estoque_1 = ItemEstoque(
            produto = self.produto1, 
            quantidade = 1
        )
        item_estoque_2 = ItemEstoque(
            produto = self.produto2, 
            quantidade = 0
        )
        item_estoque_3 = ItemEstoque(
            produto = self.produto3, 
            quantidade = 4
        )
        item_estoque_4 = ItemEstoque(
            produto = self.produto4, 
            quantidade = 10
        )
        produtos = {
            self.produto1.id: item_estoque_1,
            self.produto2.id: item_estoque_2,
            self.produto3.id: item_estoque_3,
            self.produto4.id: item_estoque_4
        }
        estoque = Estoque(produtos)

        lista_produtos_retorno = estoque.listar_produtos_estoque(min_valor = 3.4, max_valor = 10)
        self.assertEqual(lista_produtos_retorno, [self.produto1, self.produto3])

    def test_listar_produtos_estoque_filtro_preco_filtros_invalidos(self):

        item_estoque_1 = ItemEstoque(
            produto = self.produto1, 
            quantidade = 1
        )
        item_estoque_2 = ItemEstoque(
            produto = self.produto2, 
            quantidade = 0
        )
        item_estoque_3 = ItemEstoque(
            produto = self.produto3, 
            quantidade = 4
        )
        item_estoque_4 = ItemEstoque(
            produto = self.produto4, 
            quantidade = 10
        )
        produtos = {
            self.produto1.id: item_estoque_1,
            self.produto2.id: item_estoque_2,
            self.produto3.id: item_estoque_3,
            self.produto4.id: item_estoque_4
        }
        estoque = Estoque(produtos)

        with self.assertRaises(ValueError) as context:
            estoque.listar_produtos_estoque(min_valor = 3.6, max_valor = 2)
        self.assertTrue("Filtros inválidos" in str(context.exception))