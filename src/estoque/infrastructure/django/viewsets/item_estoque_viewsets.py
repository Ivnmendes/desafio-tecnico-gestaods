from dataclasses import asdict

from dependency_injector.wiring import Provide, inject
from drf_spectacular.utils import (
    OpenApiParameter,
    extend_schema,
    extend_schema_view,
    inline_serializer,
)
from rest_framework import serializers, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from estoque.domain.exceptions import ProdutoIndisponivelError
from estoque.infrastructure.django.containers import Container
from estoque.infrastructure.django.filters.item_estoque_filters import (
    FiltroPrecoFilterSet,
)
from estoque.infrastructure.django.models import ItemEstoqueModel
from estoque.infrastructure.django.serializers.item_estoque_serializer import (
    AjustarQuantidadeSerializer,
    ItemEstoqueCreateUpdateSerializer,
    ItemEstoqueRetrieveSerializer,
)


@extend_schema_view(
    list=extend_schema(
        parameters=[
            OpenApiParameter(
                name="preco_min",
                type=float,
                location=OpenApiParameter.QUERY,
                description="Filtro para preço mínimo (>=)",
            ),
            OpenApiParameter(
                name="preco_max",
                type=float,
                location=OpenApiParameter.QUERY,
                description="Filtro para preço máximo (<=)",
            ),
        ],
        responses={
            200: ItemEstoqueRetrieveSerializer(many=True),
            400: inline_serializer(
                "ErroFiltros", fields={"error": serializers.CharField()}
            ),
        },
        description="Lista todos os itens do estoque com filtros de preço",
    ),
    create=extend_schema(
        request=ItemEstoqueCreateUpdateSerializer,
        responses={
            201: ItemEstoqueRetrieveSerializer,
            404: inline_serializer(
                "ErroProdutoIndisponivel", fields={"error": serializers.CharField()}
            ),
            400: inline_serializer(
                "ErroValidacao", fields={"detail": serializers.DictField()}
            ),
        },
    ),
    retrieve=extend_schema(
        responses={200: ItemEstoqueRetrieveSerializer, 404: None},
        description="Obtém um ItemEstoque pelo id do produto",
    ),
    destroy=extend_schema(
        responses={204: None, 404: None},
        description="Remove um ItemEstoque do banco pelo id do produto",
    ),
    ajustar_quantidade=extend_schema(
        request=AjustarQuantidadeSerializer,
        responses={
            201: ItemEstoqueRetrieveSerializer,
            400: inline_serializer(
                "ErroValidacao", fields={"detail": serializers.DictField()}
            ),
            404: inline_serializer(
                "ErroProdutoIndisponivel", fields={"error": serializers.CharField()}
            ),
        },
        description="Altera a quantidade de um item em estoque",
    ),
    total_produtos=extend_schema(
        responses={
            200: inline_serializer(
                "TotalProdutos", fields={"total_produtos": serializers.IntegerField()}
            )
        }
    ),
    total_valor=extend_schema(
        responses={
            200: inline_serializer(
                "TotalValorResponse", fields={"total_valor": serializers.FloatField()}
            )
        },
        description="Retorna o valor financeiro total do estoque somado",
    ),
    verificar_estoque=extend_schema(
        responses={
            "disponivel": inline_serializer(
                "InfoEstoqueResponse",
                fields={
                    "id": serializers.UUIDField(),
                    "nome": serializers.CharField(),
                    "valor_individual": serializers.FloatField(),
                    "quantidade": serializers.IntegerField(),
                },
            ),
            404: inline_serializer(
                "ErroProdutoIndisponivel", fields={"error": serializers.CharField()}
            ),
        }
    ),
)
class ItemEstoqueViewSet(viewsets.ViewSet):

    @inject
    def __init__(
        self,
        repo_estoque=Provide[Container.repo_estoque],
        repo_produto=Provide[Container.repo_produto],
        adicionar_produto_ao_estoque_use_case=Provide[
            Container.adicionar_produtos_use_case
        ],
        ajustar_quantidade_produto_use_case=Provide[
            Container.ajustar_quantidade_produto_use_case
        ],
        filtrar_produtos_estoque_use_case=Provide[
            Container.filtrar_produtos_estoque_use_case
        ],
        total_produtos_estoque_use_case=Provide[
            Container.total_produtos_estoque_use_case
        ],
        total_valor_estoque_use_case=Provide[Container.total_valor_estoque_use_case],
        verificar_estoque_produto_use_case=Provide[
            Container.verificar_estoque_produto_use_case
        ],
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.repo_estoque = repo_estoque
        self.repo_produto = repo_produto
        self.adicionar_produto_ao_estoque_use_case = (
            adicionar_produto_ao_estoque_use_case
        )
        self.ajustar_quantidade_produto_use_case = ajustar_quantidade_produto_use_case
        self.filtrar_produtos_estoque_use_case = filtrar_produtos_estoque_use_case
        self.total_produtos_estoque_use_case = total_produtos_estoque_use_case
        self.total_valor_estoque_use_case = total_valor_estoque_use_case
        self.verificar_estoque_produto_use_case = verificar_estoque_produto_use_case

    def list(self, request):

        filtro = FiltroPrecoFilterSet(
            data=request.query_params, queryset=ItemEstoqueModel.objects.none()
        )

        if not filtro.is_valid():
            return Response(filtro.errors, status=400)

        dados = filtro.form.cleaned_data
        print(dados)

        if dados.get("preco_min") is not None or dados.get("preco_max") is not None:
            preco_min = (
                dados.get("preco_min") if dados.get("preco_min") is not None else 0.0
            )
            preco_max = dados.get("preco_max")
            itens_estoque = self.filtrar_produtos_estoque_use_case.execute(
                preco_minimo=preco_min, preco_maximo=preco_max
            )
        else:
            itens_estoque = self.repo_estoque.obter_todos_itens_estoque()

        serializer = ItemEstoqueRetrieveSerializer(itens_estoque, many=True)
        return Response(serializer.data)

    def create(self, request):

        serializer = ItemEstoqueCreateUpdateSerializer(data=request.data)

        if serializer.is_valid():

            try:
                item_estoque = self.adicionar_produto_ao_estoque_use_case.execute(
                    serializer.validated_data["produto_id"],
                    serializer.validated_data["quantidade"],
                )
            except ProdutoIndisponivelError as e:
                return Response({"error": str(e)}, status=404)

            return Response(
                ItemEstoqueRetrieveSerializer(item_estoque).data, status=201
            )

        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):

        item_estoque = self.repo_estoque.obter_item_estoque(pk)
        if item_estoque is not None:
            serializer = ItemEstoqueRetrieveSerializer(item_estoque)
            return Response(serializer.data)
        return Response(status=404)

    def destroy(self, request, pk=None):

        item_estoque = self.repo_estoque.obter_item_estoque(pk)
        if item_estoque is not None:
            self.repo_estoque.remover(pk)
            return Response(status=204)
        return Response(status=404)

    @action(detail=True, methods=["patch"])
    def ajustar_quantidade(self, request, pk=None):

        serializer = AjustarQuantidadeSerializer(data=request.data)

        if serializer.is_valid():
            try:
                self.ajustar_quantidade_produto_use_case.execute(
                    pk, serializer.validated_data["quantidade"]
                )
            except ProdutoIndisponivelError as e:
                return Response({"error": str(e)}, status=404)
            except ValueError as e:
                return Response({"error": str(e)}, status=400)
        else:
            return Response(serializer.errors, status=400)

        item_estoque = self.repo_estoque.obter_item_estoque(pk)
        serializer = ItemEstoqueRetrieveSerializer(item_estoque)
        return Response(serializer.data)

    @action(detail=False, methods=["get"])
    def total_produtos(self, request):

        total = self.total_produtos_estoque_use_case.execute()

        return Response({"total_produtos": total})

    @action(detail=False, methods=["get"])
    def total_valor(self, request):

        total = self.total_valor_estoque_use_case.execute()

        return Response({"total_valor": total})

    @action(detail=True, methods=["get"])
    def verificar_estoque(self, request, pk=None):

        try:
            disponivel = self.verificar_estoque_produto_use_case.execute(pk)
        except ProdutoIndisponivelError as e:
            return Response({"error": str(e)}, status=404)

        return Response({"disponivel": asdict(disponivel)}, status=200)
