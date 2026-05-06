from estoque.domain.repositories import IEstoqueRepository


class FiltrarEstoquePorPrecoUseCase:

    def __init__(self, estoque_repo: IEstoqueRepository):
        self.repositorio_estoque = estoque_repo

    def execute(
        self, preco_minimo: float = 0.0, preco_maximo: float | None = None
    ) -> list:

        if preco_minimo < 0:
            raise ValueError("O preço mínimo não pode ser negativo.")
        if preco_maximo is not None and preco_maximo < 0:
            raise ValueError("O preço máximo não pode ser negativo.")
        if preco_maximo is not None and preco_minimo > preco_maximo:
            raise ValueError("O preço mínimo não pode ser maior que o preço máximo.")

        return self.repositorio_estoque.filtrar_itens_estoque_preco(
            preco_minimo, preco_maximo
        )
