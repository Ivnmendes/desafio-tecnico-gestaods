
import uuid

from .value_objects import NomeProduto, Preco

class Produto():
    
    def __init__(self, nome: NomeProduto, preco: Preco):
        
        self._id = str(uuid.uuid4())
        self._nome = nome
        self._preco = preco

    def __str__(self):
        return f"{self.nome} - R${round(self.preco, 2)}"
    
    @property
    def nome(self):
        return self._nome

    @property
    def preco(self):
        return self._preco
    
    def alterar_preco(self, preco: Preco) -> None: self._preco = preco