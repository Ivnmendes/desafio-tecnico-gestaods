from src.estoque.infrastructure.MemoryEstoqueRepository import MemoryEstoqueRepository
from tests.estoque.domain.contract_tests import EstoqueRepositoryContract


class TestMemoryEstoqueRepository(EstoqueRepositoryContract):

    def create_repository(self):
        return MemoryEstoqueRepository()
