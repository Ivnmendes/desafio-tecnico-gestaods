from unittest import TestCase
from unittest.mock import Mock

from estoque.application.use_cases.verificar_estoque_produto import (
    VerificarEstoqueProdutoUseCase,
)
from estoque.domain.exceptions import ProdutoIndisponivelError
from estoque.domain.repositories import IEstoqueRepository
from produto.domain.entities import Produto
from produto.domain.repositories import IProdutoRepository


class TestVerificarEstoqueProduto(TestCase):

    def setUp(self):

        self.estoque_repo = Mock(spec=IEstoqueRepository)
        self.produto_repo = Mock(spec=IProdutoRepository)

    def test_verificar_estoque_produto_sucesso(self):

        produto = Produto(id="123", nome="Produto A", preco=50.0)

        self.estoque_repo.obter_item_estoque.return_value = Mock(
            produto_id=produto.id, quantidade=10
        )
        self.produto_repo.obter_produto.return_value = Mock(
            nome="Produto A", preco=50.0
        )

        resultado = VerificarEstoqueProdutoUseCase(
            self.estoque_repo, self.produto_repo
        ).execute(produto)

        self.assertEqual(resultado.id, produto.id)
        self.assertEqual(resultado.nome, "Produto A")
        self.assertEqual(resultado.valor_individual, 50.0)
        self.assertEqual(resultado.quantidade, 10)

    def test_verificar_estoque_produto_indisponivel(self):

        produto = Produto(id="123", nome="Produto A", preco=50.0)
        self.estoque_repo.obter_item_estoque.return_value = None

        with self.assertRaises(ProdutoIndisponivelError):
            VerificarEstoqueProdutoUseCase(
                self.estoque_repo, self.produto_repo
            ).execute(produto)

    def test_verificar_estoque_produto_produto_nao_encontrado(self):

        produto = Produto(id="123", nome="Produto A", preco=50.0)
        self.estoque_repo.obter_item_estoque.return_value = Mock(
            produto_id=produto.id, quantidade=10
        )
        self.produto_repo.obter_produto.return_value = None

        with self.assertRaises(ProdutoIndisponivelError):
            VerificarEstoqueProdutoUseCase(
                self.estoque_repo, self.produto_repo
            ).execute(produto)
