from abc import ABC, abstractmethod

from .entities import Produto


class IProdutoRepository(ABC):
    """Interface para o repositório de produtos."""

    @abstractmethod
    def salvar(self, produto: Produto) -> Produto:
        """Salva um produto no repositório."""
        pass

    @abstractmethod
    def obter_produto(self, produto_id: str) -> Produto | None:
        """Recupera um produto do repositório com base no ID, retornando None se não encontrado."""
        pass

    @abstractmethod
    def obter_todos_produtos(self) -> list[Produto]:
        """Recupera todos os produtos do repositório."""
        pass

    @abstractmethod
    def remover(self, produto_id: str) -> None:
        """Remove um produto do repositório com base no ID."""
        pass

    @abstractmethod
    def buscar_por_ids(self, produto_ids: list[str]) -> list[Produto]:
        """Busca produtos no repositório com base em uma lista de IDs, retornando os produtos encontrados."""
        pass
