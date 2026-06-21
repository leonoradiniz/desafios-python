# Desafio 6 — Criação de Matrizes: `random` vs `NumPy`

Comparação entre duas formas de criar matrizes com valores aleatórios em Python.

## Arquivos

### [uso_random.py](src/uso_random.py)
Cria uma matriz 3x3 usando apenas a biblioteca nativa `random`. A construção é manual: dois laços `for` aninhados percorrem linhas e colunas, e cada valor é gerado com `random.randint()` e adicionado a uma lista.

### [uso_np.py](src/uso_np.py)
Cria a mesma matriz 3x3 usando `NumPy`. Uma única linha — `np.random.randint()` com o parâmetro `size=(3, 3)` — substitui toda a lógica manual do exemplo anterior.

## O que aprender com esse desafio

| | `random` | `NumPy` |
|---|---|---|
| Dependência | Biblioteca nativa | Biblioteca externa |
| Linhas de código | Mais verboso | Muito conciso |
| Legibilidade | Exige laços explícitos | Declarativo |
| Adequado para | Scripts simples, sem dependências externas | Cálculos matemáticos e manipulação de dados |

A comparação evidencia como o NumPy reduz a complexidade do código ao abstrair operações que, com `random`, exigem controle manual de estrutura de dados.