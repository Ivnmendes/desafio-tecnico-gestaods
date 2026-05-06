from unittest import TestCase
from unittest.mock import Mock

from estoque.domain.exceptions import ProdutoIndisponivelError
from produto.application.use_cases.alterar_valor_produto import (
    AlterarValorProdutoUseCase,
)
from produto.domain.entities import Produto
from produto.domain.repositories import IProdutoRepository


class TestAlterarValorProduto(TestCase):

    def test_alterar_valor_produto(self):

        produto_repository = Mock(spec=IProdutoRepository)
        produto = Produto(id="produto-1", nome="Produto A", preco=100.0)
        produto_repository.obter_produto.return_value = produto

        AlterarValorProdutoUseCase(produto_repository).execute("produto-1", 150.0)

        self.assertEqual(produto.preco, 150.0)
        produto_repository.salvar.assert_called_once_with(produto)

    def test_alterar_valor_produto_produto_nao_encontrado(self):

        produto_repository = Mock(spec=IProdutoRepository)
        produto_repository.obter_produto.return_value = None

        with self.assertRaises(ProdutoIndisponivelError) as context:
            AlterarValorProdutoUseCase(produto_repository).execute("produto-1", 150.0)

        self.assertEqual(str(context.exception), "Produto não encontrado.")
