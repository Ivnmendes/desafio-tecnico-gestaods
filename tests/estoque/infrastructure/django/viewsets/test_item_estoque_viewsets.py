import uuid

import pytest
from rest_framework.test import APIClient

from estoque.infrastructure.django.models import ItemEstoqueModel
from produto.infrastructure.django.models import ProdutoModel


@pytest.mark.django_db
def test_listar_estoque_retorna_200():
    client = APIClient()

    response = client.get("/api/estoque/")

    assert response.status_code == 200
    assert isinstance(response.data, list)


@pytest.mark.django_db
def test_listar_estoque_com_filtro_retorna_200():
    client = APIClient()

    response = client.get("/api/estoque/?preco_min=10&preco_max=100")

    assert response.status_code == 200
    assert isinstance(response.data, list)


@pytest.mark.django_db
def test_listar_estoque_com_filtro_invalido_retorna_400():
    client = APIClient()

    response = client.get("/api/estoque/?preco_min=abc")

    assert response.status_code == 400
    assert "preco_min" in response.data


@pytest.mark.django_db
def test_criar_item_estoque_retorna_201():
    client = APIClient()

    produto = ProdutoModel.objects.create(
        nome="Produto Teste",
        preco=50.0,
    )

    payload = {"produto_id": produto.id, "quantidade": 10}

    response = client.post("/api/estoque/", data=payload, format="json")

    assert response.status_code == 201
    assert response.data["quantidade"] == 10
    assert response.data["produto"]["id"] == str(produto.id)
    assert response.data["produto"]["nome"] == produto.nome
    assert float(response.data["produto"]["preco"]) == float(produto.preco)
    assert "id" in response.data

    assert ItemEstoqueModel.objects.filter(id=response.data["id"]).exists()
    item_no_banco = ItemEstoqueModel.objects.get(id=response.data["id"])
    assert item_no_banco.produto_id == produto.id
    assert item_no_banco.quantidade == 10


@pytest.mark.django_db
def test_criar_item_estoque_com_dados_invalidos_retorna_400():
    client = APIClient()
    payload = {"produto_id": "", "quantidade": 3}

    response = client.post("/api/estoque/", data=payload, format="json")

    assert response.status_code == 400
    assert "produto_id" in response.data


@pytest.mark.django_db
def test_criar_item_estoque_com_produto_inexistente_retorna_404():
    client = APIClient()
    payload = {"produto_id": str(uuid.uuid4()), "quantidade": 10}

    response = client.post("/api/estoque/", data=payload, format="json")

    assert response.status_code == 404
    assert "error" in response.data


@pytest.mark.django_db
def test_retriever_item_estoque_retorna_200():
    client = APIClient()

    produto = ProdutoModel.objects.create(
        nome="Produto Teste",
        preco=50.0,
    )
    ItemEstoqueModel.objects.create(
        produto=produto,
        quantidade=10,
    )

    response = client.get(f"/api/estoque/{produto.id}/")

    assert response.status_code == 200
    assert response.data["quantidade"] == 10
    assert response.data["produto"]["id"] == str(produto.id)
    assert response.data["produto"]["nome"] == produto.nome
    assert float(response.data["produto"]["preco"]) == float(produto.preco)


@pytest.mark.django_db
def test_retriever_item_estoque_inexistente_retorna_404():
    client = APIClient()

    response = client.get(f"/api/estoque/{uuid.uuid4()}/")

    assert response.status_code == 404


@pytest.mark.django_db
def test_destroy_item_estoque_retorna_204():
    client = APIClient()

    produto = ProdutoModel.objects.create(
        nome="Produto Teste",
        preco=50.0,
    )
    item_estoque = ItemEstoqueModel.objects.create(
        produto=produto,
        quantidade=10,
    )

    response = client.delete(f"/api/estoque/{produto.id}/")

    assert response.status_code == 204
    assert not ItemEstoqueModel.objects.filter(id=item_estoque.id).exists()


@pytest.mark.django_db
def test_destroy_item_estoque_inexistente_retorna_404():
    client = APIClient()

    response = client.delete(f"/api/estoque/{uuid.uuid4()}/")

    assert response.status_code == 404


@pytest.mark.django_db
def test_ajustar_quantidade_item_estoque_retorna_200():
    client = APIClient()

    produto = ProdutoModel.objects.create(
        nome="Produto Teste",
        preco=50.0,
    )
    item_estoque = ItemEstoqueModel.objects.create(
        produto=produto,
        quantidade=10,
    )

    payload = {"quantidade": 5}
    response = client.patch(
        f"/api/estoque/{produto.id}/ajustar_quantidade/", data=payload, format="json"
    )

    assert response.status_code == 200
    assert response.data["quantidade"] == 15
    assert response.data["produto"]["id"] == str(produto.id)
    assert response.data["produto"]["nome"] == produto.nome
    assert float(response.data["produto"]["preco"]) == float(produto.preco)

    assert ItemEstoqueModel.objects.filter(id=item_estoque.id, quantidade=15).exists()
    item_estoque_atualizado = ItemEstoqueModel.objects.get(id=item_estoque.id)
    assert item_estoque_atualizado.quantidade == 15


@pytest.mark.django_db
def test_ajustar_quantidade_item_estoque_com_dados_invalidos_retorna_400():
    client = APIClient()

    produto = ProdutoModel.objects.create(
        nome="Produto Teste",
        preco=50.0,
    )
    ItemEstoqueModel.objects.create(
        produto=produto,
        quantidade=10,
    )

    payload = {"quantidade": "abc"}
    response = client.patch(
        f"/api/estoque/{produto.id}/ajustar_quantidade/", data=payload, format="json"
    )

    assert response.status_code == 400
    assert "quantidade" in response.data


@pytest.mark.django_db
def test_ajustar_quantidade_item_estoque_inexistente_retorna_404():
    client = APIClient()

    payload = {"quantidade": 5}
    response = client.patch(
        f"/api/estoque/{uuid.uuid4()}/ajustar_quantidade/", data=payload, format="json"
    )

    assert response.status_code == 404

    assert "error" in response.data


@pytest.mark.django_db
def test_ajustar_quantidade_item_estoque_com_dados_faltando_retorna_400():
    client = APIClient()

    produto = ProdutoModel.objects.create(
        nome="Produto Teste",
        preco=50.0,
    )
    ItemEstoqueModel.objects.create(
        produto=produto,
        quantidade=10,
    )

    payload: dict = {}
    response = client.patch(
        f"/api/estoque/{produto.id}/ajustar_quantidade/", data=payload, format="json"
    )

    assert response.status_code == 400
    assert "quantidade" in response.data


@pytest.mark.django_db
def test_ajustar_quantidade_item_resultado_negativo_retorna_400():
    client = APIClient()

    produto = ProdutoModel.objects.create(
        nome="Produto Teste",
        preco=50.0,
    )
    ItemEstoqueModel.objects.create(
        produto=produto,
        quantidade=10,
    )

    payload = {"quantidade": -15}
    response = client.patch(
        f"/api/estoque/{produto.id}/ajustar_quantidade/", data=payload, format="json"
    )

    assert response.status_code == 400
    assert "negativo" in response.data["error"].lower()


@pytest.mark.django_db
def test_total_produtos_retorna_200():
    client = APIClient()

    produto1 = ProdutoModel.objects.create(
        nome="Produto Teste 1",
        preco=50.0,
    )
    ItemEstoqueModel.objects.create(
        produto=produto1,
        quantidade=10,
    )

    produto2 = ProdutoModel.objects.create(
        nome="Produto Teste 2",
        preco=30.0,
    )
    ItemEstoqueModel.objects.create(
        produto=produto2,
        quantidade=5,
    )

    response = client.get("/api/estoque/total_produtos/")

    assert response.status_code == 200
    assert response.data["total_produtos"] == 15


@pytest.mark.django_db
def test_total_produtos_com_estoque_vazio_retorna_200():
    client = APIClient()

    response = client.get("/api/estoque/total_produtos/")

    assert response.status_code == 200
    assert response.data["total_produtos"] == 0


@pytest.mark.django_db
def test_total_valor_estoque_retorna_200():
    client = APIClient()

    produto1 = ProdutoModel.objects.create(
        nome="Produto Teste 1",
        preco=50.0,
    )
    ItemEstoqueModel.objects.create(
        produto=produto1,
        quantidade=10,
    )

    produto2 = ProdutoModel.objects.create(
        nome="Produto Teste 2",
        preco=30.0,
    )
    ItemEstoqueModel.objects.create(
        produto=produto2,
        quantidade=5,
    )

    response = client.get("/api/estoque/total_valor/")

    assert response.status_code == 200
    assert float(response.data["total_valor"]) == 650.0


@pytest.mark.django_db
def test_total_valor_estoque_com_estoque_vazio_retorna_200():
    client = APIClient()

    response = client.get("/api/estoque/total_valor/")

    assert response.status_code == 200
    assert float(response.data["total_valor"]) == 0.0


@pytest.mark.django_db
def test_verificar_estoque_produto_retorna_200():
    client = APIClient()

    produto = ProdutoModel.objects.create(
        nome="Produto Teste",
        preco=50.0,
    )
    ItemEstoqueModel.objects.create(
        produto=produto,
        quantidade=10,
    )

    response = client.get(f"/api/estoque/{produto.id}/verificar_estoque/")

    assert response.status_code == 200
    assert "disponivel" in response.data
    assert response.data["disponivel"]["id"] == produto.id
    assert response.data["disponivel"]["nome"] == produto.nome
    assert float(response.data["disponivel"]["valor_individual"]) == float(
        produto.preco
    )
    assert response.data["disponivel"]["quantidade"] == 10


@pytest.mark.django_db
def test_verificar_estoque_produto_inexistente_retorna_404():
    client = APIClient()

    response = client.get(f"/api/estoque/{uuid.uuid4()}/verificar_estoque/")

    assert response.status_code == 404
    assert "error" in response.data
