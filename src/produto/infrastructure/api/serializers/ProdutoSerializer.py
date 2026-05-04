from rest_framework import serializers


class ProdutoSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    nome = serializers.CharField(max_length=255)
    preco = serializers.DecimalField(max_digits=10, decimal_places=2)
