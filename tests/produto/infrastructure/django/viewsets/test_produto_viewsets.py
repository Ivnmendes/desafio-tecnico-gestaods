import uuid

import pytest
from rest_framework.test import APIClient

from produto.infrastructure.django.models import ProdutoModel


@pytest.mark.django_db
def test_listar_produtos_retorna_200():
    client = APIClient()

    response = client.get("/api/produtos/")

    assert response.status_code == 200
    assert isinstance(response.data, list)


@pytest.mark.django_db
def test_criar_produto_retorna_201():
    client = APIClient()

    payload = {"nome": "Produto Teste", "preco": 50.0}

    response = client.post("/api/produtos/", data=payload, format="json")

    assert response.status_code == 201
    assert response.data["nome"] == payload["nome"]
    assert float(response.data["preco"]) == payload["preco"]
    assert "id" in response.data

    assert ProdutoModel.objects.filter(id=response.data["id"]).exists()


@pytest.mark.django_db
def test_criar_produto_com_dados_invalidos_retorna_400():
    client = APIClient()

    payload = {"nome": "", "preco": -10.0}

    response = client.post("/api/produtos/", data=payload, format="json")

    assert response.status_code == 400
    assert "nome" in response.data
    assert "preco" in response.data


@pytest.mark.django_db
def test_retriever_produto_retorna_200():
    client = APIClient()

    produto = ProdutoModel.objects.create(
        nome="Produto Teste",
        preco=50.0,
    )

    response = client.get(f"/api/produtos/{produto.id}/")

    assert response.status_code == 200
    assert response.data["id"] == str(produto.id)
    assert response.data["nome"] == produto.nome
    assert float(response.data["preco"]) == float(produto.preco)


@pytest.mark.django_db
def test_retriever_produto_inexistente_retorna_404():
    client = APIClient()

    produto_id_inexistente = uuid.uuid4()

    response = client.get(f"/api/produtos/{produto_id_inexistente}/")

    assert response.status_code == 404


@pytest.mark.django_db
def test_atualizar_preco_produto_retorna_200():
    client = APIClient()

    produto = ProdutoModel.objects.create(
        nome="Produto Teste",
        preco=50.0,
    )

    payload = {"preco": 75.0}

    response = client.patch(
        f"/api/produtos/{produto.id}/atualizar_preco/", data=payload, format="json"
    )

    assert response.status_code == 200
    assert float(response.data["preco"]) == payload["preco"]


@pytest.mark.django_db
def test_atualizar_preco_produto_com_dados_invalidos_retorna_400():
    client = APIClient()

    produto = ProdutoModel.objects.create(
        nome="Produto Teste",
        preco=50.0,
    )

    payload = {"preco": -20.0}

    response = client.patch(
        f"/api/produtos/{produto.id}/atualizar_preco/", data=payload, format="json"
    )

    assert response.status_code == 400
    assert "preco" in response.data


@pytest.mark.django_db
def test_atualizar_preco_produto_inexistente_retorna_404():
    client = APIClient()

    produto_id_inexistente = uuid.uuid4()

    payload = {"preco": 75.0}

    response = client.patch(
        f"/api/produtos/{produto_id_inexistente}/atualizar_preco/",
        data=payload,
        format="json",
    )

    assert response.status_code == 404


@pytest.mark.django_db
def test_destroy_produto_retorna_204():
    client = APIClient()

    produto = ProdutoModel.objects.create(
        nome="Produto Teste",
        preco=50.0,
    )

    response = client.delete(f"/api/produtos/{produto.id}/")

    assert response.status_code == 204
    assert not ProdutoModel.objects.filter(id=produto.id).exists()


@pytest.mark.django_db
def test_destroy_produto_inexistente_retorna_404():
    client = APIClient()

    produto_id_inexistente = uuid.uuid4()

    response = client.delete(f"/api/produtos/{produto_id_inexistente}/")

    assert response.status_code == 404
