from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from produto.application.use_cases.alterar_valor_produto import alterar_valor_produto
from produto.application.use_cases.criar_produto import criar_produto
from produto.infrastructure.django.repositories.DjangoProdutoRepository import (
    DjangoProdutoRepository,
)
from produto.infrastructure.django.serializers.ProdutoSerializer import (
    ProdutoSerializer,
)


class ProdutoViewSet(viewsets.ViewSet):

    repo_produto = DjangoProdutoRepository()

    def list(self, request):

        produtos = self.repo_produto.obter_todos_produtos()

        serializer = ProdutoSerializer(produtos, many=True)

        return Response(serializer.data)

    def create(self, request):

        serializer = ProdutoSerializer(data=request.data)

        if serializer.is_valid():

            produto = criar_produto(
                serializer.validated_data["nome"],
                serializer.validated_data["preco"],
                self.repo_produto,
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
            produto = alterar_valor_produto(
                pk, request.data.get("preco"), self.repo_produto
            )
        except ValueError as e:
            return Response({"error": str(e)}, status=400)

        serializer = ProdutoSerializer(produto)
        return Response(serializer.data)

    def destroy(self, request, pk=None):

        self.repo_produto.remover(pk)
        return Response(status=204)
