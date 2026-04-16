
from produto import Produto

class Estoque():

    @property
    def disponivel(self):
        return self._disponivel
    
    def __init__(self, disponivel: list[dict[Produto: int]] = None):

        if not disponivel:
            self._disponivel = []
            return

        if any(quantidade < 0 for item in disponivel for quantidade in item.values()):
            raise Exception("O estoque de nenhum produto pode ser negativo!")
        
        self._disponivel = list(disponivel)