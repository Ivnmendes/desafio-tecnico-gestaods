from dependency_injector.wiring import Provide, inject
from drf_spectacular.utils import extend_schema, extend_schema_view, inline_serializer
from rest_framework import serializers, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from estoque.domain.exceptions import ProdutoIndisponivelError
from produto.infrastructure.django.containers import Container
from produto.infrastructure.django.serializers.produto_serializer import (
    AlterarValorProdutoSerializer,
    ProdutoSerializer,
)


@extend_schema_view(
    list=extend_schema(
        summary="Listar produtos",
        description="Retorna todos os produtos cadastrados no catálogo.",
        responses={200: ProdutoSerializer(many=True)},
    ),
    create=extend_schema(
        summary="Criar produto",
        description="Cadastra um novo produto validando as regras de negócio do domínio.",
        request=ProdutoSerializer,
        responses={
            201: ProdutoSerializer,
            400: inline_serializer(
                "ErroCriacaoProduto", fields={"detail": serializers.DictField()}
            ),
        },
    ),
    retrieve=extend_schema(
        summary="Obter produto",
        description="Busca os detalhes de um produto específico pelo seu ID (UUID).",
        responses={200: ProdutoSerializer, 404: None},
    ),
    atualizar_preco=extend_schema(
        summary="Atualizar preço",
        description="Altera o valor de venda de um produto existente.",
        request=AlterarValorProdutoSerializer,
        responses={
            200: ProdutoSerializer,
            400: inline_serializer(
                "ErroValidacaoPreco", fields={"detail": serializers.DictField()}
            ),
            404: inline_serializer(
                "ErroProdutoNaoEncontradoPreco",
                fields={"error": serializers.CharField()},
            ),
        },
    ),
    destroy=extend_schema(
        summary="Remover produto",
        description="Exclui o produto do sistema.",
        responses={204: None, 404: None},
    ),
)
class ProdutoViewSet(viewsets.ViewSet):

    @inject
    def __init__(
        self,
        repo_produto=Provide[Container.repo_produto],
        alterar_valor_produto_use_case=Provide[
            Container.alterar_valor_produto_use_case
        ],
        criar_produto_use_case=Provide[Container.criar_produto_use_case],
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.repo_produto = repo_produto
        self.alterar_valor_produto_use_case = alterar_valor_produto_use_case
        self.criar_produto_use_case = criar_produto_use_case

    def list(self, request):

        produtos = self.repo_produto.obter_todos_produtos()

        serializer = ProdutoSerializer(produtos, many=True)

        return Response(serializer.data)

    def create(self, request):

        serializer = ProdutoSerializer(data=request.data)

        if serializer.is_valid():

            produto = self.criar_produto_use_case.execute(
                nome=serializer.validated_data["nome"],
                preco=serializer.validated_data["preco"],
            )

            return Response(ProdutoSerializer(produto).data, status=201)

        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):

        produto = self.repo_produto.obter_produto(pk)
        if produto is not None:
            serializer = ProdutoSerializer(produto)
            return Response(serializer.data)
        return Response(status=404)

    @action(detail=True, methods=["patch"])
    def atualizar_preco(self, request, pk=None):

        serializer = AlterarValorProdutoSerializer(data=request.data)

        if serializer.is_valid():
            try:
                produto = self.alterar_valor_produto_use_case.execute(
                    pk, request.data.get("preco")
                )
            except ProdutoIndisponivelError:
                return Response(status=404)

            serializer = ProdutoSerializer(produto)
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):

        produto = self.repo_produto.obter_produto(pk)
        if produto is not None:
            self.repo_produto.remover(pk)
            return Response(status=204)
        return Response(status=404)
