from dataclasses import dataclass


@dataclass(frozen=True)
class InfoEstoqueDTO:
    id: str
    nome: str
    valor_individual: float
    quantidade: int
