from produto.domain.entities import Produto
from produto.domain.repositories import IProdutoRepository
from produto.infrastructure.django.models import ProdutoModel


class DjangoProdutoRepository(IProdutoRepository):

    def salvar(self, produto: Produto) -> Produto:

        produto, _ = ProdutoModel.objects.update_or_create(
            id=produto.id, defaults={"nome": produto.nome, "preco": produto.preco}
        )
        return produto

    def obter_produto(self, produto_id: str) -> Produto | None:

        try:
            model = ProdutoModel.objects.get(id=produto_id)
            return Produto(id=model.id, nome=model.nome, preco=model.preco)
        except ProdutoModel.DoesNotExist:
            return None

    def obter_todos_produtos(self) -> list[Produto]:

        return [
            Produto(id=model.id, nome=model.nome, preco=model.preco)
            for model in ProdutoModel.objects.all().iterator()
        ]

    def remover(self, produto_id: str) -> None:
        ProdutoModel.objects.filter(id=produto_id).delete()

    def buscar_por_ids(self, produto_ids: list[str]) -> list[Produto]:

        return [
            Produto(id=model.id, nome=model.nome, preco=model.preco)
            for model in ProdutoModel.objects.filter(id__in=produto_ids)
        ]

    def filtrar_produtos_preco(
        self, preco_min: float, preco_max: float | None = None
    ) -> list[Produto]:

        filters = {"preco__gte": preco_min}
        if preco_max is not None:
            filters["preco__lte"] = preco_max

        queryset = ProdutoModel.objects.filter(**filters)

        return [
            Produto(id=model.id, nome=model.nome, preco=model.preco)
            for model in queryset
        ]
