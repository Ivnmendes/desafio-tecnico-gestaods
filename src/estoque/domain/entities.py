from produto.domain.entities import Produto

from .value_objects import Quantidade


class ItemEstoque:
    """Representa um item no estoque, associando um produto a uma quantidade."""

    def __init__(self, produto: Produto, quantidade: int) -> None:

        self._quantidade = Quantidade(quantidade)
        self._produto = produto

    def __repr__(self) -> str:
        return (
            f"ItemEstoque(produto={repr(self._produto)}, quantidade={self.quantidade})"
        )

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
        """
        Ajusta o saldo do estoque.

        Aceita valores negativos, desde que o saldo final não fique negativo.
        """
        self._quantidade = self._quantidade.somar(qtd)
