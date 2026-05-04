import uuid
from abc import ABC, abstractmethod

from produto.domain.entities import Produto


class ProdutoRepositoryContract(ABC):

    @abstractmethod
    def create_repository(self):
        """Método factory que deve ser sobrescrito."""
        pass

    def test_deve_salvar_e_recuperar_produto(self):

        repo = self.create_repository()
        id = str(uuid.uuid4())
        produto = Produto(id=id, nome="Produto A", preco=10.0)

        repo.salvar(produto)
        resultado = repo.obter_produto(id)

        assert resultado.nome == "Produto A", "Nome do produto não corresponde"
        assert resultado.preco == 10.0, "Preço do produto não corresponde"

    def test_deve_remover_produto(self):

        repo = self.create_repository()
        id = str(uuid.uuid4())
        produto = Produto(id=id, nome="Produto A", preco=10.0)

        repo.salvar(produto)
        repo.remover(id)
        resultado = repo.obter_produto(id)

        assert resultado is None

    def test_deve_obter_todos_produtos(self):

        repo = self.create_repository()
        id1 = str(uuid.uuid4())
        id2 = str(uuid.uuid4())
        produto1 = Produto(id=id1, nome="Produto A", preco=10.0)
        produto2 = Produto(id=id2, nome="Produto B", preco=20.0)

        repo.salvar(produto1)
        repo.salvar(produto2)
        resultado = repo.obter_todos_produtos()

        assert len(resultado) == 2, "Número de produtos obtidos não corresponde"
        assert id1 in [
            str(p.id) for p in resultado
        ], "ID do primeiro produto não corresponde"
        assert id2 in [
            str(p.id) for p in resultado
        ], "ID do segundo produto não corresponde"

    def test_deve_lancar_erro_ao_obter_produto_inexistente(self):

        repo = self.create_repository()

        produto = repo.obter_produto(str(uuid.uuid4()))

        assert produto is None

    def test_deve_buscar_por_ids(self):

        repo = self.create_repository()
        id1 = str(uuid.uuid4())
        id2 = str(uuid.uuid4())
        produto1 = Produto(id=id1, nome="Produto A", preco=10.0)
        produto2 = Produto(id=id2, nome="Produto B", preco=20.0)

        repo.salvar(produto1)
        repo.salvar(produto2)

        resultado = repo.buscar_por_ids([id1, id2])

        assert len(resultado) == 2, "Número de produtos obtidos não corresponde"
        assert id1 in [
            str(p.id) for p in resultado
        ], "ID do primeiro produto não corresponde"
        assert id2 in [
            str(p.id) for p in resultado
        ], "ID do segundo produto não corresponde"

    def test_filtrar_produtos_por_preco(self):

        repo = self.create_repository()
        id1 = str(uuid.uuid4())
        id2 = str(uuid.uuid4())
        id3 = str(uuid.uuid4())
        produto1 = Produto(id=id1, nome="Produto A", preco=10.0)
        produto2 = Produto(id=id2, nome="Produto B", preco=20.0)
        produto3 = Produto(id=id3, nome="Produto C", preco=30.0)

        repo.salvar(produto1)
        repo.salvar(produto2)
        repo.salvar(produto3)

        resultado = repo.filtrar_produtos_preco(15.0)

        assert len(resultado) == 2, "Número de produtos obtidos não corresponde"
        assert id2 in [
            str(p.id) for p in resultado
        ], "ID do primeiro produto não corresponde"
        assert id3 in [
            str(p.id) for p in resultado
        ], "ID do segundo produto não corresponde"

    def test_filtrar_produtos_por_preco_com_maximo(self):

        repo = self.create_repository()
        id1 = str(uuid.uuid4())
        id2 = str(uuid.uuid4())
        id3 = str(uuid.uuid4())
        produto1 = Produto(id=id1, nome="Produto A", preco=10.0)
        produto2 = Produto(id=id2, nome="Produto B", preco=20.0)
        produto3 = Produto(id=id3, nome="Produto C", preco=30.0)

        repo.salvar(produto1)
        repo.salvar(produto2)
        repo.salvar(produto3)

        resultado = repo.filtrar_produtos_preco(15.0, 25.0)

        assert len(resultado) == 1, "Número de produtos obtidos não corresponde"
        assert id2 in [str(p.id) for p in resultado], "ID do produto não corresponde"
