# Exercícios com Listas em Python

Projeto acadêmico com vários exemplos práticos de manipulação de listas em Python.

---

## 📁 Estrutura do Projeto

```
desafio-3-listas/
│
├── listaNotasAlunos.py     # Lista combinada de alunos e suas respectivas notas
├── listaNumeros.py         # Operações com pilha (stack) em uma lista de números inteiros
├── listaMatriz.py          # Matriz bidimensional de números para praticar listas aninhadas
├── listComprehension.py    # Criação de uma lista de quadrados de 1 a 5 através de iterações
└── README.md
```

---

## Descrição dos Exercícios

### `listaNotasAlunos.py`
Combina duas listas — nomes de alunos e suas notas — em uma única lista intercalada usando `zip()`. Demonstra o uso de:
- `append()` para construir a lista
- Slicing com índices positivos e negativos
- Loop `for` e loop `while` para iteração
- `remove()` para exclusão de elementos
- Concatenação de listas com `+`

### `listaNumeros.py`
Simula o comportamento de uma **pilha (stack)** com uma lista de números. Demonstra o uso de:
- `append()` para empilhar elementos
- `pop()` para desempilhar o último elemento
- `len()` para obter o tamanho da lista
- `sort()` para ordenação crescente
- `reverse()` para inversão da lista

### `listaMatriz.py`
Cria e acessa elementos de uma **matriz 3x3** usando listas aninhadas. Demonstra o uso de:
- Indexação dupla `matriz[linha][coluna]`

### `listComprehension.py`
Gera uma lista de quadrados de 1 a 5 através de iterações, usando **List Comprehension**. Demonstra o uso de:
- Sintaxe `[expressão for variável in iterável]`
- `range()` para definir o intervalo

---

## ▶️ Como Executar

Clone o repositório do GitHub para sua máquina através do comando ```git clone```.
Certifique-se de ter o **Python 3** instalado. Para rodar cada exercício individualmente, abra o projeto na sua IDE de preferência, e escreva no terminal:

```bash
python listaNotasAlunos.py
python listaNumeros.py
python listaMatriz.py
python listComprehension.py
```

---