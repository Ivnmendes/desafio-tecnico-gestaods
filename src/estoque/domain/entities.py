
from typing import TypedDict

from src.produto.domain.entities import Produto
from .exceptions import ProdutoIndisponivelError
from .value_objects import Quantidade

class ItemEstoque():
    
    def __init__(self, produto: Produto, quantidade: int) -> None:

        self._quantidade = Quantidade(quantidade)
        self._produto = produto

    @property
    def quantidade(self):
        return self._quantidade
    
    @property
    def produto(self):
        return self._produto
    
    def ajustar_quantidade(self, qtd: int) -> None:
        self._quantidade = self._quantidade.somar(qtd)

class InfoEstoqueDict(TypedDict):
    nome: str
    valor_individual: float
    quantidade: int
    
class Estoque():

    def __init__(self, itens: dict[str, ItemEstoque] = None) -> None:
        self._itens = itens if itens is not None else {}

    @property
    def itens(self):
        return self._itens
    
    def adicionar_produto(self, produto: Produto, qtd: int) -> None:

        if produto.id in self._itens:
            self._itens[produto.id].ajustar_quantidade(qtd)
            return
        
        self._itens[produto] = ItemEstoque(produto, qtd)

    def remover_produto(self, produto: Produto) -> None:

        if produto.id not in self._itens:
            raise ProdutoIndisponivelError("Produto não encontrado no estoque!")
        
        del self._itens[produto.id]

    def total_valor_estoque(self) -> float:

        if not self._itens:
            return 0

        return sum(item.produto.preco.valor * item.quantidade.valor for item in self._itens.values())
    
    def total_produtos_estoque(self) -> int:

        if not self._itens:
            return 0
        
        return sum(item.quantidade.valor for item in self._itens.values())

    def verificar_estoque_produto(self, produto: Produto) -> InfoEstoqueDict:

        if produto.id not in self._itens:
            raise ProdutoIndisponivelError("Produto não encontrado no estoque!")
        
        item = self._itens[produto.id]

        return InfoEstoqueDict( 
            nome = item.produto.nome.valor, 
            valor_individual = item.produto.preco.valor, 
            quantidade = item.quantidade.valor
        )
    
    def limpar_estoque(self) -> None: self._itens.clear()

    def listar_produtos_estoque(self, min_valor = 0, max_valor = None) -> list[Produto]:

        if max_valor is not None and (min_valor > max_valor):
            raise ValueError("Filtros inválidos: O valor mínimo não pode ser maior que o valor máximo.")

        if min_valor < 0:
            raise ValueError("Filtros inválidos: O valor mínimo não pode ser negativo.")
        
        produtos_filtrados = []

        for item in self._itens.values():
            if item.produto.preco.valor < min_valor:
                continue
                
            if max_valor is not None and item.produto.preco.valor > max_valor:
                continue
                
            produtos_filtrados.append(item.produto)

        return produtos_filtrados
    
    def ajustar_quantidade_produto(self, produto: Produto, qtd: int) -> None:
        if produto.id not in self._itens:
            raise ProdutoIndisponivelError("Produto não disponível no estoque!")
        
        self._itens[produto.id].ajustar_quantidade(qtd)