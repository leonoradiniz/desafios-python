# 🧮 Desafio 5 — Matrizes em Python

Projeto acadêmico de estudo e prática de matrizes em Python, com exercícios que cobrem desde a criação e manipulação manual até o uso da biblioteca NumPy.

## 📂 Estrutura do projeto

```
desafio-5/
├── src/
│   ├── matrizes.py              # Anotações de estudo sobre matrizes
│   ├── matrizes_np.py           # Operações com matrizes usando NumPy
│   └── exercicios_praticos/
│       ├── ex_1.py              # Matriz 3x3 com valores aleatórios
│       ├── ex_2.py              # Soma de vendas de duas semanas
│       ├── ex_3.py              # Média de notas por aluno (NumPy)
│       ├── ex_4.py              # Verificação e cálculo de matriz inversa
│       └── ex_5.py              # Cálculo de valor em estoque
```

## 📑 Conteúdo

### `src/matrizes.py`
Anotações de aprendizado sobre matrizes em Python usando listas aninhadas:
- Criação de uma matriz de notas de alunos
- Acesso e modificação de elementos por índice
- Cálculo de média manual
- Adição e subtração de matrizes com loops aninhados

### `src/matrizes_np.py`
Uso da biblioteca NumPy para operações de álgebra linear:
- Cálculo do determinante com `np.linalg.det`
- Cálculo da matriz inversa com `np.linalg.inv`

### Exercícios práticos

| Exercício | Descrição |
|-----------|-----------|
| `ex_1.py` | Gera e exibe uma matriz 3x3 preenchida com inteiros aleatórios entre 1 e 100 |
| `ex_2.py` | Some as vendas diárias de duas semanas (matrizes 7x1) para obter o total da quinzena |
| `ex_3.py` | Calcula a média de notas de 5 alunos (3 notas cada) usando `np.mean` com `axis=1` |
| `ex_4.py` | Verifica se uma matriz 3x3 é invertível e exibe sua inversa, caso exista |
| `ex_5.py` | Multiplica elemento a elemento as matrizes de estoque e preços para calcular o valor total em estoque |

## Requisitos

- Python 3.x
- NumPy (`pip install numpy`)

## ▶️ Como executar

```bash
python src/matrizes.py
python src/exercicios_praticos/ex_1.py
# ... e assim por diante para cada exercício
```
