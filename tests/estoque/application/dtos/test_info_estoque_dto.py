from dataclasses import FrozenInstanceError
from typing import Any
from unittest import TestCase

from src.estoque.application.dtos.InfoEstoqueDTO import InfoEstoqueDTO


class TestInfoEstoqueDTO(TestCase):

    def test_deve_criar_dto_com_dados_validos(self):
        dto = InfoEstoqueDTO(
            id="produto-1",
            nome="Caneta",
            valor_individual=2.5,
            quantidade=3,
        )

        self.assertEqual("produto-1", dto.id)
        self.assertEqual("Caneta", dto.nome)
        self.assertEqual(2.5, dto.valor_individual)
        self.assertEqual(3, dto.quantidade)

    def test_dto_deve_ser_imutavel(self):
        dto = InfoEstoqueDTO(
            id="produto-1",
            nome="Caneta",
            valor_individual=2.5,
            quantidade=3,
        )

        with self.assertRaises(FrozenInstanceError):
            dto_as_any: Any = dto
            dto_as_any.nome = "Lapis"
