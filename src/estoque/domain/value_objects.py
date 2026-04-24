class Quantidade:

    def __init__(self, valor: int):

        if valor < 0:
            raise ValueError("O estoque não pode ser negativo!")
        self._valor = valor

    def somar(self, outra_quantidade: int) -> "Quantidade":

        if outra_quantidade + self._valor < 0:
            raise ValueError("O estoque não pode ser negativo!")

        return Quantidade(self._valor + outra_quantidade)

    @property
    def valor(self) -> int:
        return self._valor
