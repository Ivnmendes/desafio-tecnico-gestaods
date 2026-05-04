from unittest import TestCase
from unittest.mock import Mock

from src.produto.application.use_cases.criar_produto import criar_produto
from src.produto.domain.entities import Produto
from src.produto.domain.repositories import IProdutoRepository


class TestCriarProduto(TestCase):

    def test_criar_produto(self):

        produto_repository = Mock(spec=IProdutoRepository)
        produto_repository.salvar.side_effect = lambda produto: Produto(
            id="produto-1", nome=produto.nome, preco=produto.preco
        )
        nome = "Produto Teste"
        preco = 10.0

        produto_criado = criar_produto(nome, preco, produto_repository)

        self.assertIsInstance(produto_criado, Produto)
        self.assertEqual(produto_criado.nome, nome)
        self.assertEqual(produto_criado.preco, preco)
