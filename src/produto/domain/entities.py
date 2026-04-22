
import uuid

from .value_objects import NomeProduto, Preco

class Produto():
    
    def __init__(self, nome: str, preco: float):
        
        self._id = str(uuid.uuid4())
        self._nome = NomeProduto(nome)
        self._preco = Preco(preco)

    def __str__(self):
        return f"{self.nome.valor} - R${round(self.preco.valor, 2)}"
    
    @property
    def nome(self):
        return self._nome

    @property
    def preco(self):
        return self._preco
    
    @property
    def id(self):
        return self._id
    
    def alterar_preco(self, preco: float) -> None: self._preco = Preco(preco)