from dependency_injector import containers, providers

from produto.application.use_cases.alterar_valor_produto import (
    AlterarValorProdutoUseCase,
)
from produto.application.use_cases.criar_produto import CriarProdutoUseCase
from produto.infrastructure.django.repositories.django_produto_repositorie import (
    DjangoProdutoRepository,
)


class Container(containers.DeclarativeContainer):

    repo_produto = providers.Singleton(DjangoProdutoRepository)

    alterar_valor_produto_use_case: providers.Singleton[AlterarValorProdutoUseCase] = (
        providers.Singleton(
            AlterarValorProdutoUseCase,
            produto_repo=repo_produto,
        )
    )

    criar_produto_use_case: providers.Singleton[CriarProdutoUseCase] = (
        providers.Singleton(
            CriarProdutoUseCase,
            produto_repo=repo_produto,
        )
    )
