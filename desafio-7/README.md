# Resolução de Sistemas de Equações Lineares com Matrizes em Python

Exercícios desenvolvidos com o objetivo de praticar a resolução de sistemas de equações lineares usando representação matricial e a biblioteca NumPy.

---

## Sobre o Projeto

Um sistema de equações lineares pode ser representado na forma matricial **AX = B**, onde:

- **A** — matriz dos coeficientes
- **X** — vetor das variáveis (incógnitas)
- **B** — vetor dos termos independentes

A solução é obtida por **X = A⁻¹B**, ou diretamente via `numpy.linalg.solve(A, B)`, que é mais eficiente e numericamente estável.

Cada exercício modela um problema prático do mundo real como um sistema linear, formula a matriz A e o vetor B correspondentes, resolve com NumPy e verifica o resultado substituindo nas equações originais.

## Exercícios

### Exercício 1 — Fábrica com Dois Recursos 

Uma fábrica produz itens usando **trabalhadores** e **máquinas**. A partir de dois dias de produção, determina-se a taxa de produção por trabalhador (x) e por máquina (y).

**Sistema:**
```
5x + 3y = 110
8x + 2y = 100
```

**Solução esperada:** x = 10,00 itens/trabalhador | y = 20,00 itens/máquina

Também calcula a produção estimada com 10 trabalhadores e 4 máquinas.

---

### Exercício 2 — Fábrica com Três Recursos 

Extensão do exercício anterior, agora com um terceiro recurso: **horas de operação**. Determina-se x (taxa por trabalhador), y (taxa por máquina) e z (taxa por hora).

**Sistema:**
```
4x + 2y + 3z = 150
3x + 3y + 2z = 140
5x +  y + 4z = 160
```

**Solução esperada:** x = 20,00 | y = 25,00 | z = 15,00

Também calcula a produção estimada com 6 trabalhadores, 3 máquinas e 5 horas. Inclui verificação do determinante antes de resolver.

---

### Exercício 3 — Padaria 

Uma padaria produz **pães e bolos** consumindo farinha e açúcar. O objetivo é determinar o consumo de farinha por pão (x) e de açúcar por bolo (y).

**Sistema:**
```
50x + 20y = 30
30x + 30y = 12
```

**Solução esperada:** x = 0,40 kg/pão | y = 0,50 kg/bolo

Também estima o consumo para 40 pães e 25 bolos.

---

### Exercício 4 — Mistura Química 

Uma empresa produz misturas usando dois compostos, **A e B**, que contêm o ingrediente ativo X. O objetivo é determinar a concentração de X por litro de A (x) e por litro de B (y).

**Sistema:**
```
60x + 40y = 26
50x + 30y = 20
```

**Solução esperada:** x = 0,30 unid/litro de A | y = 0,20 unid/litro de B

Também estima as unidades de X em uma mistura com 70 litros de A e 50 litros de B.

---

## Conceitos Praticados

- Representação matricial de sistemas lineares (AX = B)
- Cálculo do determinante com `numpy.linalg.det`
- Resolução de sistemas com `numpy.linalg.solve`
- Tratamento de erros com `try-except` para matrizes singulares
- Verificação de soluções por substituição nas equações originais