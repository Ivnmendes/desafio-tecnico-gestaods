from produto.domain.entities import Produto

from .value_objects import Quantidade


class ItemEstoque:

    def __init__(self, produto: Produto, quantidade: int) -> None:

        self._quantidade = Quantidade(quantidade)
        self._produto = produto

    def __repr__(self) -> str:
        return f"ItemEstoque(produto={self._produto.id}, quantidade={self.quantidade})"

    @property
    def quantidade(self):
        return self._quantidade.valor

    @property
    def produto_id(self):
        return self._produto.id

    @property
    def produto(self):
        return self._produto

    def ajustar_quantidade(self, qtd: int) -> None:
        self._quantidade = self._quantidade.somar(qtd)
