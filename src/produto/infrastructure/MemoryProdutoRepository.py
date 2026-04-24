from produto.domain.repositories import IProdutoRepository


class MemoryProdutoRepository(IProdutoRepository):

    def __init__(self):
        self.produtos = {}

    def salvar(self, produto):
        self.produtos[produto.id] = produto

    def obter_produto(self, produto_id):
        return self.produtos.get(produto_id)

    def obter_todos_produtos(self):
        return list(self.produtos.values())

    def remover(self, produto_id):
        if produto_id in self.produtos:
            del self.produtos[produto_id]

    def buscar_por_ids(self, produto_ids):
        return [self.produtos[pid] for pid in produto_ids if pid in self.produtos]
