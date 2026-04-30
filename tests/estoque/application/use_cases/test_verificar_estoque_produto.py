from unittest import TestCase
from unittest.mock import Mock

from estoque.application.use_cases.verificar_estoque_produto import (
    verificar_estoque_produto,
)
from estoque.domain.exceptions import ProdutoIndisponivelError
from estoque.domain.repositories import IEstoqueRepository
from produto.domain.repositories import IProdutoRepository


class TestVerificarEstoqueProduto(TestCase):

    def setUp(self):

        self.estoque_repo = Mock(spec=IEstoqueRepository)
        self.produto_repo = Mock(spec=IProdutoRepository)

    def test_verificar_estoque_produto_sucesso(self):

        produto_id = "123"

        self.estoque_repo.obter_item_estoque.return_value = Mock(
            produto_id=produto_id, quantidade=10
        )
        self.produto_repo.obter_produto.return_value = Mock(
            nome="Produto A", preco=50.0
        )

        resultado = verificar_estoque_produto(
            self.estoque_repo, self.produto_repo, produto_id
        )

        self.assertEqual(resultado.id, produto_id)
        self.assertEqual(resultado.nome, "Produto A")
        self.assertEqual(resultado.valor_individual, 50.0)
        self.assertEqual(resultado.quantidade, 10)

    def test_verificar_estoque_produto_indisponivel(self):

        produto_id = "123"
        self.estoque_repo.obter_item_estoque.return_value = None

        with self.assertRaises(ProdutoIndisponivelError):
            verificar_estoque_produto(self.estoque_repo, self.produto_repo, produto_id)

    def test_verificar_estoque_produto_produto_nao_encontrado(self):

        produto_id = "123"
        self.estoque_repo.obter_item_estoque.return_value = Mock(
            produto_id=produto_id, quantidade=10
        )
        self.produto_repo.obter_produto.return_value = None

        with self.assertRaises(ProdutoIndisponivelError):
            verificar_estoque_produto(self.estoque_repo, self.produto_repo, produto_id)
