from dependency_injector import containers, providers

from produto.infrastructure.django.repositories.django_produto_repositorie import (
    DjangoProdutoRepository,
)


class Container(containers.DeclarativeContainer):
    repo_produto = providers.Factory(DjangoProdutoRepository)
