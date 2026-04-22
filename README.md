# Missão TDD - GestãoDS

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

## Estrutura de testes

Os testes estão organizados em:

- `tests/produto`
- `tests/estoque`

Cobrem cenários positivos e negativos de regras de negócio, incluindo validações e mensagens de erro.

## Como rodar os testes

### 1) Criar e ativar ambiente virtual (opcional, recomendado)

```bash
python -m venv venv
source venv/bin/activate
```

### 2) Executar todos os testes

```bash
python -m unittest discover -s tests -t . -v
```

### 3) Executar testes por módulo

```bash
python -m unittest tests/produto/domain/test_entities.py -v
python -m unittest tests/estoque/domain/test_entities.py -v
```
