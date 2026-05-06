from dependency_injector.wiring import Provide, inject
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from estoque.domain.exceptions import ProdutoIndisponivelError
from produto.infrastructure.django.containers import Container
from produto.infrastructure.django.serializers.produto_serializer import (
    ProdutoSerializer,
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

        if not request.data.get("preco"):
            return Response({"error": 'O campo "preco" é obrigatório.'}, status=400)

        try:
            produto = self.alterar_valor_produto_use_case.execute(
                pk, request.data.get("preco")
            )
        except ValueError as e:
            return Response({"error": str(e)}, status=400)
        except ProdutoIndisponivelError:
            return Response(status=404)

        serializer = ProdutoSerializer(produto)
        return Response(serializer.data)

    def destroy(self, request, pk=None):

        self.repo_produto.remover(pk)
        return Response(status=204)
