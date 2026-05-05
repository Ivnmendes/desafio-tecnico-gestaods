from abc import ABC, abstractmethod

from .entities import ItemEstoque


class IEstoqueRepository(ABC):
    """Contrato para repositórios de estoque."""

    @abstractmethod
    def salvar(self, item_estoque: ItemEstoque) -> ItemEstoque:
        """Insere um novo item no estoque ou atualiza um item existente, retornando o item salvo."""
        pass

    @abstractmethod
    def remover(self, produto_id: str) -> None:
        """Remove um item do estoque com base no ID do produto."""
        pass

    @abstractmethod
    def obter_item_estoque(self, produto_id: str) -> ItemEstoque | None:
        """Recupera um item do estoque com base no ID do produto, retornando None se não encontrado."""
        pass

    @abstractmethod
    def obter_todos_itens_estoque(self) -> list[ItemEstoque]:
        """Recupera todos os itens atualmente disponíveis no estoque."""
        pass

    @abstractmethod
    def limpar_estoque(self) -> None:
        """Limpa todo o estoque."""
        pass

    @abstractmethod
    def filtrar_itens_estoque_preco(
        self, preco_minimo: float = 0.0, preco_maximo: float | None = None
    ) -> list[ItemEstoque]:
        """Filtra os itens do estoque com base em um intervalo de preço."""
        pass
