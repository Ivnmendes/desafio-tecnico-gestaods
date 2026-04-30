from .value_objects import Quantidade


class ItemEstoque:

    def __init__(self, produto_id: str, quantidade: int) -> None:

        self._quantidade = Quantidade(quantidade)
        self._produto_id = produto_id

    def __repr__(self) -> str:
        return f"ItemEstoque(produto={self._produto_id}, quantidade={self.quantidade})"

    @property
    def quantidade(self):
        return self._quantidade.valor

    @property
    def produto_id(self):
        return self._produto_id

    def ajustar_quantidade(self, qtd: int) -> None:
        self._quantidade = self._quantidade.somar(qtd)
