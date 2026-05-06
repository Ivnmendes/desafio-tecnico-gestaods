from rest_framework import serializers

from produto.infrastructure.django.serializers.produto_serializer import (
    ProdutoSerializer,
)


class ItemEstoqueRetrieveSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    produto = ProdutoSerializer()
    quantidade = serializers.IntegerField()


class ItemEstoqueCreateUpdateSerializer(serializers.Serializer):
    produto_id = serializers.UUIDField()
    quantidade = serializers.IntegerField()

    def validate_quantidade(self, value):
        if value < 0:
            raise serializers.ValidationError("A quantidade não pode ser negativa.")
        return value


class AjustarQuantidadeSerializer(serializers.Serializer):
    quantidade = serializers.IntegerField()
