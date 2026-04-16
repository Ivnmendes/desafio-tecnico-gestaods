
from produto import Produto

class Estoque():

    @property
    def disponivel(self):
        return self._disponivel
    
    def __init__(self, lista_estoque: list[dict[Produto, int]] = None):

        if not lista_estoque:
            self._disponivel = {}
            return

        self._disponivel = {}

        for item in lista_estoque:
            for produto, quantidade in item.items():
                if quantidade < 0:
                    raise ValueError("O estoque de nenhum produto pode ser negativo!")

                self._disponivel[produto] = self._disponivel.get(produto, 0) + quantidade

    def total_valor_estoque(self):
        if not self.disponivel:
            return 0

        return sum(prod.valor * qtd for prod, qtd in self._disponivel.items())
    
    def total_produtos_estoque(self):
        if not self.disponivel:
            return 0
        
        return sum(qtd for _, qtd in self._disponivel.items())