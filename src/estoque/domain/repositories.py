from abc import ABC, abstractmethod

from .entities import ItemEstoque


class IEstoqueRepository(ABC):

    @abstractmethod
    def salvar(self, item_estoque: ItemEstoque) -> ItemEstoque:
        pass

    @abstractmethod
    def remover(self, produto_id: str) -> None:
        pass

    @abstractmethod
    def obter_item_estoque(self, produto_id: str) -> ItemEstoque | None:
        pass

    @abstractmethod
    def obter_todos_itens_estoque(self) -> list[ItemEstoque]:
        pass

    @abstractmethod
    def limpar_estoque(self) -> None:
        pass

    @abstractmethod
    def filtrar_itens_estoque_preco(
        self, preco_minimo: float = 0.0, preco_maximo: float | None = None
    ) -> list[ItemEstoque]:
        pass
