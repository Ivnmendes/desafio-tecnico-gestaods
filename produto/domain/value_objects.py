
class NomeProduto:

    def __init__(self, nome: str):

        if not nome or not nome.strip():
            raise ValueError("Não é possível iniciar um produto com nome vazio!")
        self._valor = nome.strip()

    @property
    def valor(self) -> str:
        return self._valor
    
class Preco:

    def __init__(self, valor: float):
        
        if valor <= 0:
            raise ValueError("O valor não pode ser zerado/negativo!")
        self._valor = round(valor, 2)

    @property
    def valor(self) -> float:
        return self._valor