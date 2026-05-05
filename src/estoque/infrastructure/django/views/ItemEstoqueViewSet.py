from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from estoque.application.use_cases.adicionar_produto_ao_estoque import (
    adicionar_produto_ao_estoque,
)
from estoque.application.use_cases.ajustar_quantidade_produto import (
    ajustar_quantidade_produto,
)
from estoque.application.use_cases.filtrar_estoque_por_preco import (
    filtrar_estoque_por_preco,
)
from estoque.application.use_cases.total_produtos_estoque import total_produtos_estoque
from estoque.application.use_cases.total_valor_estoque import total_valor_estoque
from estoque.application.use_cases.verificar_estoque_produto import (
    verificar_estoque_produto,
)
from estoque.domain.exceptions import ProdutoIndisponivelError
from estoque.infrastructure.django.repositories.DjangoEstoqueRepository import (
    DjangoEstoqueRepository,
)
from estoque.infrastructure.django.serializers.ItemEstoqueSerializer import (
    ItemEstoqueCreateUpdateSerializer,
    ItemEstoqueRetrieveSerializer,
)
from produto.infrastructure.django.repositories.DjangoProdutoRepository import (
    DjangoProdutoRepository,
)


class ItemEstoqueViewSet(viewsets.ViewSet):

    repo_estoque = DjangoEstoqueRepository()
    repo_produto = DjangoProdutoRepository()

    def list(self, request):

        preco_min = request.query_params.get("preco_min")
        preco_max = request.query_params.get("preco_max")

        if preco_min is not None or preco_max is not None:
            kwargs = {}
            try:
                if preco_min is not None:
                    kwargs["preco_minimo"] = float(preco_min)
                if preco_max is not None:
                    kwargs["preco_maximo"] = float(preco_max)

                itens_estoque = filtrar_estoque_por_preco(self.repo_estoque, **kwargs)
            except ValueError as e:
                return Response({"error": str(e)}, status=400)
        else:
            itens_estoque = self.repo_estoque.obter_todos_itens_estoque()

        serializer = ItemEstoqueRetrieveSerializer(itens_estoque, many=True)

        return Response(serializer.data)

    def create(self, request):

        serializer = ItemEstoqueCreateUpdateSerializer(data=request.data)

        if serializer.is_valid():

            try:
                item_estoque = adicionar_produto_ao_estoque(
                    self.repo_estoque,
                    self.repo_produto,
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

        if not request.data.get("quantidade"):
            return Response(
                {"error": 'O campo "quantidade" é obrigatório.'}, status=400
            )

        try:
            ajustar_quantidade_produto(
                self.repo_estoque, pk, request.data.get("quantidade")
            )
        except ProdutoIndisponivelError as e:
            return Response({"error": str(e)}, status=404)

        item_estoque = self.repo_estoque.obter_item_estoque(pk)
        serializer = ItemEstoqueRetrieveSerializer(item_estoque)
        return Response(serializer.data)

    @action(detail=False, methods=["get"])
    def total_produtos(self, request):

        total = total_produtos_estoque(self.repo_estoque)

        return Response({"total_produtos": total})

    @action(detail=False, methods=["get"])
    def total_valor(self, request):

        total = total_valor_estoque(self.repo_estoque, self.repo_produto)

        return Response({"total_valor": total})

    @action(detail=False, methods=["get"])
    def filtrar_por_preco(self, request):

        preco_min = request.query_params.get("preco_min")
        preco_max = request.query_params.get("preco_max")

        if preco_min is None or preco_max is None:
            return Response(
                {"error": 'Os parâmetros "preco_min" e "preco_max" são obrigatórios.'},
                status=400,
            )

        try:
            itens_filtrados = filtrar_estoque_por_preco(
                self.repo_estoque, float(preco_min), float(preco_max)
            )
        except ValueError:
            return Response(
                {"error": 'Os parâmetros "preco_min" e "preco_max" devem ser números.'},
                status=400,
            )

        serializer = ItemEstoqueRetrieveSerializer(itens_filtrados, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=["get"])
    def verificar_estoque(self, request, pk=None):

        try:
            disponivel = verificar_estoque_produto(
                self.repo_estoque, self.repo_produto, pk
            )
        except ProdutoIndisponivelError as e:
            return Response({"error": str(e)}, status=404)

        return Response({"disponivel": disponivel})
