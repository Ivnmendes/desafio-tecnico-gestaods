from dependency_injector import containers, providers

from produto.application.use_cases.alterar_valor_produto import (
    AlterarValorProdutoUseCase,
)
from produto.application.use_cases.criar_produto import CriarProdutoUseCase
from produto.infrastructure.django.repositories.django_produto_repositorie import (
    DjangoProdutoRepository,
)


class Container(containers.DeclarativeContainer):

    repo_produto = providers.Factory(DjangoProdutoRepository)

    alterar_valor_produto_use_case: providers.Factory[AlterarValorProdutoUseCase] = (
        providers.Factory(
            AlterarValorProdutoUseCase,
            produto_repo=repo_produto,
        )
    )

    criar_produto_use_case: providers.Factory[CriarProdutoUseCase] = providers.Factory(
        CriarProdutoUseCase,
        produto_repo=repo_produto,
    )
