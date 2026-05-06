from rest_framework import serializers


class ProdutoSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    nome = serializers.CharField(max_length=255)
    preco = serializers.DecimalField(max_digits=10, decimal_places=2)

    def validate_preco(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "O preço deve ser um valor positivo maior que 0."
            )
        return value


class AlterarValorProdutoSerializer(serializers.Serializer):
    preco = serializers.DecimalField(max_digits=10, decimal_places=2)

    def validate_preco(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "O preço deve ser um valor positivo maior que 0."
            )
        return value
