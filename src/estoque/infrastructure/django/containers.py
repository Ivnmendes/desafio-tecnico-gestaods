from dependency_injector import containers, providers

from estoque.infrastructure.django.repositories.django_estoque_repositorie import (
    DjangoEstoqueRepository,
)
from produto.infrastructure.django.repositories.django_produto_repositorie import (
    DjangoProdutoRepository,
)


class Container(containers.DeclarativeContainer):
    repo_estoque = providers.Factory(DjangoEstoqueRepository)
    repo_produto = providers.Factory(DjangoProdutoRepository)
