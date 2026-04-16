
class Produto():

    @property
    def nome(self):
        return self._nome

    @property
    def valor(self):
        return self._valor
    
    def __init__(self, nome: str, valor: float):

        if not nome:
            raise Exception("Não é possível iniciar um produto com nome vazio!")
        
        if valor <= 0:
            raise Exception("Não é possível iniciar um produto com valor zerado/negativo!")
        
        self._nome = nome
        valor_normalizado = round(valor, 2)
        self._valor = valor_normalizado

    def __str__(self):
        return f"{self.nome} - R${self.valor}"
    
    def alterar_valor(self, valor: float):

        if valor <= 0:
            raise Exception("O valor não pode ser zerado/negativo!")
        
        valor_normalizado = round(valor, 2)
        self._valor = valor_normalizado