from dependency_injector import containers, providers

from estoque.application.use_cases.adicionar_produto_ao_estoque import (
    AdicionarProdutoAoEstoqueUseCase,
)
from estoque.application.use_cases.ajustar_quantidade_produto import (
    AjustarQuantidadeProdutoUseCase,
)
from estoque.application.use_cases.filtrar_estoque_por_preco import (
    FiltrarEstoquePorPrecoUseCase,
)
from estoque.application.use_cases.total_produtos_estoque import (
    TotalProdutosEstoqueUseCase,
)
from estoque.application.use_cases.total_valor_estoque import TotalValorEstoqueUseCase
from estoque.application.use_cases.verificar_estoque_produto import (
    VerificarEstoqueProdutoUseCase,
)
from estoque.infrastructure.django.repositories.django_estoque_repositorie import (
    DjangoEstoqueRepository,
)
from produto.infrastructure.django.repositories.django_produto_repositorie import (
    DjangoProdutoRepository,
)


class Container(containers.DeclarativeContainer):

    repo_estoque = providers.Factory(DjangoEstoqueRepository)
    repo_produto = providers.Factory(DjangoProdutoRepository)

    adicionar_produtos_use_case: providers.Factory[AdicionarProdutoAoEstoqueUseCase] = (
        providers.Factory(
            AdicionarProdutoAoEstoqueUseCase,
            estoque_repo=repo_estoque,
            produto_repo=repo_produto,
        )
    )

    ajustar_quantidade_produto_use_case: providers.Factory[
        AjustarQuantidadeProdutoUseCase
    ] = providers.Factory(AjustarQuantidadeProdutoUseCase, estoque_repo=repo_estoque)

    filtrar_produtos_estoque_use_case: providers.Factory[
        FiltrarEstoquePorPrecoUseCase
    ] = providers.Factory(FiltrarEstoquePorPrecoUseCase, estoque_repo=repo_estoque)

    total_produtos_estoque_use_case: providers.Factory[TotalProdutosEstoqueUseCase] = (
        providers.Factory(TotalProdutosEstoqueUseCase, estoque_repo=repo_estoque)
    )

    total_valor_estoque_use_case: providers.Factory[TotalValorEstoqueUseCase] = (
        providers.Factory(
            TotalValorEstoqueUseCase,
            estoque_repo=repo_estoque,
            produto_repo=repo_produto,
        )
    )

    verificar_estoque_produto_use_case: providers.Factory[
        VerificarEstoqueProdutoUseCase
    ] = providers.Factory(
        VerificarEstoqueProdutoUseCase,
        estoque_repo=repo_estoque,
        produto_repo=repo_produto,
    )
