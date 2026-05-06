from unittest import TestCase

from estoque.infrastructure.django.serializers.item_estoque_serializer import (
    ItemEstoqueCreateUpdateSerializer,
    ItemEstoqueRetrieveSerializer,
)


class TestItemEstoqueRetrieveSerializer(TestCase):

    def test_serializer_valido(self):

        data: dict = {
            "produto": {
                "id": "123e4567-e89b-12d3-a456-426614174001",
                "nome": "Produto Teste",
                "preco": "19.99",
            },
            "quantidade": 10,
        }

        serializer = ItemEstoqueRetrieveSerializer(data=data)

        self.assertTrue(serializer.is_valid())
        self.assertEqual(
            serializer.validated_data["produto"]["nome"], data["produto"]["nome"]
        )
        self.assertEqual(
            str(serializer.validated_data["produto"]["preco"]), data["produto"]["preco"]
        )
        self.assertEqual(serializer.validated_data["quantidade"], data["quantidade"])

    def test_serializer_invalido(self):

        data: dict = {
            "produto": {
                "nome": "Produto Teste",
                "preco": "aaaa",
            },
            "quantidade": 10,
        }

        serializer = ItemEstoqueRetrieveSerializer(data=data)

        self.assertFalse(serializer.is_valid())
        self.assertIn("produto", serializer.errors)


class TestItemEstoqueCreateUpdateSerializer(TestCase):

    def test_serializer_valido(self):

        data: dict = {
            "produto_id": "123e4567-e89b-12d3-a456-426614174001",
            "quantidade": 10,
        }

        serializer = ItemEstoqueCreateUpdateSerializer(data=data)

        self.assertTrue(serializer.is_valid())
        self.assertEqual(
            str(serializer.validated_data["produto_id"]), data["produto_id"]
        )
        self.assertEqual(serializer.validated_data["quantidade"], data["quantidade"])

    def test_serializer_invalido(self):

        data: dict = {
            "produto_id": "123e4567-e89b-12d3-a456-426614174001",
            "quantidade": -5,
        }

        serializer = ItemEstoqueCreateUpdateSerializer(data=data)

        self.assertFalse(serializer.is_valid())
        self.assertIn("quantidade", serializer.errors)
