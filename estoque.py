
from produto import Produto

class Estoque():

    @property
    def disponivel(self):
        return self._disponivel
    
    def __init__(self, lista_estoque: list[dict[Produto, int]] = None) -> None:

        if not lista_estoque:
            self._disponivel = {}
            return

        self._disponivel = {}

        for item in lista_estoque:
            for produto, quantidade in item.items():
                if quantidade < 0:
                    raise ValueError("O estoque de nenhum produto pode ser negativo!")

                self._disponivel[produto] = self._disponivel.get(produto, 0) + quantidade

    def total_valor_estoque(self) -> float:

        if not self.disponivel:
            return 0

        return sum(prod.valor * qtd for prod, qtd in self._disponivel.items())
    
    def total_produtos_estoque(self) -> int:

        if not self.disponivel:
            return 0
        
        return sum(qtd for _, qtd in self._disponivel.items())
    
    def ajustar_quantidade_produto(self, produto: Produto, qtd: int) -> None:

        if produto not in self._disponivel:
            raise Exception("Produto não disponível no estoque!")

        if self._disponivel[produto] + qtd < 0:
            raise Exception("O estoque atualizado do produto não pode ser negativo!")
        
        self._disponivel[produto] += qtd

    def adicionar_produto(self, produto: Produto, qtd: int) -> None:

        if qtd < 0:
            raise Exception("O estoque do produto não pode ser negativo!")

        if produto in self._disponivel:
            self._disponivel[produto] += qtd
            return
        
        self._disponivel[produto] = qtd

    def remover_produto(self, produto: Produto) -> None:

        if produto not in self._disponivel:
            raise Exception("Produto não encontrado no estoque!")
        
        self._disponivel.pop(produto)

    def verificar_estoque_produto(self, produto: Produto) -> dict[str: str | float | int]:

        if produto not in self._disponivel:
            raise Exception("Produto não encontrado no estoque!")
        
        quantidade_estoque = self._disponivel[produto]

        return { "nome": produto.nome, "valor_individual": produto.valor, "quantidade": quantidade_estoque}
    
    def limpar_estoque(self) -> None: self._disponivel = {}

    def listar_produtos_estoque(self, min_valor = 0, max_valor = None) -> list[Produto]:

        if max_valor is not None and (min_valor > max_valor):
            raise ValueError("Filtros inválidos: O valor mínimo não pode ser maior que o valor máximo.")

        if min_valor < 0:
            raise ValueError("Filtros inválidos: O valor mínimo não pode ser negativo.")
        
        produtos_filtrados = []

        for produto in self._disponivel.keys():
            if produto.valor < min_valor:
                continue
                
            if max_valor is not None and produto.valor > max_valor:
                continue
                
            produtos_filtrados.append(produto)

        return produtos_filtrados