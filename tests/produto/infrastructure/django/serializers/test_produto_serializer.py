from unittest import TestCase

from produto.infrastructure.django.serializers.ProdutoSerializer import (
    ProdutoSerializer,
)


class TestProdutoSerializer(TestCase):

    def test_serializer_valido(self):
        data = {"nome": "Produto Teste", "preco": "19.99"}

        serializer = ProdutoSerializer(data=data)

        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data["nome"], data["nome"])
        self.assertEqual(str(serializer.validated_data["preco"]), data["preco"])

    def test_serializer_invalido(self):
        data = {
            "nome": "Produto Teste",
            "preco": "invalid_price",
            "descricao": "Descrição do produto teste",
        }

        serializer = ProdutoSerializer(data=data)

        self.assertFalse(serializer.is_valid())
        self.assertIn("preco", serializer.errors)
