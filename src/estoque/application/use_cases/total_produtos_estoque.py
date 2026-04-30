from src.estoque.domain.repositories import IEstoqueRepository


def total_produtos_estoque(repositorio_estoque: IEstoqueRepository) -> int:

    itens = repositorio_estoque.obter_todos_itens_estoque()

    return sum(item.quantidade for item in itens)
