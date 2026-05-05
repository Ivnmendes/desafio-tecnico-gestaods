from rest_framework import serializers

from produto.infrastructure.django.serializers.ProdutoSerializer import (
    ProdutoSerializer,
)


class ItemEstoqueRetrieveSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    produto = ProdutoSerializer()
    quantidade = serializers.IntegerField()


class ItemEstoqueCreateUpdateSerializer(serializers.Serializer):
    produto_id = serializers.UUIDField()
    quantidade = serializers.IntegerField()
