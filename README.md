# Missão TDD - GestãoDS

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square&logo=python)](https://www.python.org/)
[![Django 5.2+](https://img.shields.io/badge/Django-5.2%2B-darkgreen?style=flat-square&logo=django)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/DRF-3.17%2B-red?style=flat-square)](https://www.django-rest-framework.org/)
[![pytest](https://img.shields.io/badge/pytest-9.0%2B-green?style=flat-square&logo=pytest)](https://pytest.org/)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?style=flat-square&logo=pre-commit)](https://pre-commit.com/)
[![Code Coverage](https://img.shields.io/badge/coverage-enabled-brightgreen?style=flat-square)](https://pytest-cov.readthedocs.io/)

Projeto de estudo com foco em TDD e modelagem de domínio para um cenário simples de:

- cadastro e regras de produto
- controle de estoque

## O que foi implementado

### Produto (`src/produto/domain`)

- Entidade `Produto` com `id` único (UUID), `nome` e `preço`.
- Value Objects:
  - `NomeProduto`: impede nome vazio.
  - `Preco`: impede valor menor ou igual a zero e arredonda para 2 casas.
- Regra de alteração de preço com validação.

### Estoque (`src/estoque/domain`)

- Entidade `ItemEstoque` com referência para `Produto` e `Quantidade`.
- Entidade `Estoque` com operações para:
  - adicionar produto
  - remover produto
  - ajustar quantidade (entrada/saída)
  - calcular total de itens
  - calcular valor total em estoque
  - consultar dados de um produto no estoque
  - limpar estoque
  - listar produtos com filtros de faixa de preço (`min_valor` e `max_valor`)
- Value Object `Quantidade`: não permite resultado negativo.
- Exceção de domínio `ProdutoIndisponivelError` para operações inválidas.

## Instalação

### Pré-requisitos
- Python 3.10+
- pip ou uv (gestor de pacotes recomendado)

### Passos de instalação

1. **Clone ou acesse o repositório**
```bash
cd caixa
```

2. **Crie um ambiente virtual (opcional, mas recomendado)**
```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

3. **Instale as dependências**
```bash
# Usando uv (recomendado)
uv sync

# Ou usando pip
pip install -r requirements.txt
```

4. **Execute as migrações do banco de dados**
```bash
uv run python tasks.py mig
```

5. **Crie um superusuário (opcional)**
```bash
uv run python tasks.py csu
```

## Scripts do Tasks

Execute os scripts através do arquivo `tasks.py` com `uv run`:

```bash
uv run python tasks.py [comando]
```

| Comando | Descrição |
|---------|-----------|
| `test` | Executa todos os testes com pytest |
| `tests_cov` | Executa testes com relatório de cobertura |
| `lint` | Executa verificação de qualidade de código (pre-commit) |
| `format` | Formata o código (pre-commit manual) |
| `mkmig` | Cria arquivo de migração do Django |
| `mig` | Aplica as migrações do banco de dados |
| `run` | Inicia o servidor de desenvolvimento (localhost:8000) |
| `csu` | Cria um novo superusuário |
| `cs` | Coleta arquivos estáticos |
| `shell` | Abre o shell interativo do Django |

**Exemplos:**
```bash
# Rodar testes
uv run python tasks.py test

# Rodar testes com cobertura
uv run python tasks.py tests_cov

# Formatar código
uv run python tasks.py format

# Iniciar servidor
uv run python tasks.py run
```

## API Endpoints

A API está disponível em `http://localhost:8000/api/`

### Produtos

#### Listar todos os produtos
```http
GET /api/produtos/
```

**Response (200):**
```json
[
  {
    "id": "uuid-123",
    "nome": "Produto A",
    "preco": 10.50
  }
]
```

---

#### Criar novo produto
```http
POST /api/produtos/
Content-Type: application/json
```

**Request:**
```json
{
  "nome": "Produto novo",
  "preco": 25.99
}
```

**Response (201):**
```json
{
  "id": "uuid-456",
  "nome": "Produto novo",
  "preco": 25.99
}
```

---

#### Obter detalhes de um produto
```http
GET /api/produtos/{id}/
```

**Response (200):**
```json
{
  "id": "uuid-123",
  "nome": "Produto A",
  "preco": 10.50
}
```

---

#### Atualizar preço de um produto
```http
PATCH /api/produtos/{id}/atualizar_preco/
Content-Type: application/json
```

**Request:**
```json
{
  "preco": 15.99
}
```

**Response (200):**
```json
{
  "id": "uuid-123",
  "nome": "Produto A",
  "preco": 15.99
}
```

---

#### Deletar um produto
```http
DELETE /api/produtos/{id}/
```

**Response (204):** No content

## Como rodar os testes

### Executar todos os testes
```bash
uv run python tasks.py test
```

### Executar testes com relatório de cobertura
```bash
uv run python tasks.py tests_cov
```

### Executar testes de um módulo específico
```bash
uv run python -m unittest tests/produto/domain/test_entities.py -v
uv run python -m unittest tests/estoque/domain/test_entities.py -v
```

## Estrutura de testes

Os testes estão organizados em:

- `tests/produto` - Testes relativos à entidade Produto
- `tests/estoque` - Testes relativos ao módulo de Estoque

Cobrem cenários positivos e negativos de regras de negócio, incluindo validações e mensagens de erro.

## Arquitetura

O projeto segue a arquitetura de **Clean Architecture** com as seguintes camadas:

### `domain/`
- **Entidades**: Regras de negócio fundamentais
- **Value Objects**: Objetos que representam valores
- **Repositórios**: Interfaces para persistência
- **Exceções**: Exceções de domínio

### `application/`
- **Use Cases**: Casos de uso da aplicação
- **DTOs**: Data Transfer Objects

### `infrastructure/`
- **Django Models**: Modelos do banco de dados
- **Repositórios**: Implementações dos repositórios
- **API**: Views e Serializers do Django REST Framework
