from abc import ABC, abstractmethod

from .entities import Produto


class IProdutoRepository(ABC):

    @abstractmethod
    def salvar(self, produto: Produto) -> None:
        pass

    @abstractmethod
    def obter_produto(self, produto_id: str) -> Produto:
        pass

    @abstractmethod
    def obter_todos_produtos(self) -> list[Produto]:
        pass

    @abstractmethod
    def remover(self, produto_id: str) -> None:
        pass

    @abstractmethod
    def buscar_por_ids(self, produto_ids: list[str]) -> list[Produto]:
        pass
