# 🛍️ Loja Simples

Sistema de simulação de loja desenvolvido em Python, com cadastro de produtos, realização de vendas, cálculo de descontos e geração de relatórios.

---

## 📁 Estrutura do projeto

```
.
├── loja_main.py       # Fluxo de execução central (menu e navegação)
├── loja_funcoes.py    # Funções e regras de negócio
└── README.md
```

---

## ▶️ Como executar

1. Clone este repositório para sua máquina.
2. No terminal, execute:

```bash
python loja_main.py
```

Nenhuma biblioteca externa é necessária — o projeto usa apenas a biblioteca padrão do Python.

---

## Funcionalidades

### Menu principal

```
========== Loja Simples ==========
1. Cadastrar produto
2. Realizar venda
3. Gerar relatório
4. Salvar relatório em arquivo
5. Sair
==================================
```

### 1. Cadastrar produto
Solicita nome, preço e estoque inicial. Validações aplicadas:
- Nome não pode ser vazio nem duplicado (insensível a maiúsculas)
- Preço deve ser um número maior que zero (aceita vírgula ou ponto)
- Estoque deve ser um número inteiro maior ou igual a zero

### 2. Realizar venda
Solicita nome do cliente, exibe os produtos disponíveis e permite selecionar por índice. Validações aplicadas:
- Nome do cliente não pode ser vazio
- Índice deve corresponder a um produto existente com estoque disponível
- Quantidade deve ser inteira, maior que zero e não superior ao estoque

Após a venda, o estoque do produto é atualizado automaticamente e um resumo é exibido.

### 3. Gerar relatório
Exibe no terminal o detalhamento de todas as vendas realizadas e o total arrecadado pela loja.

### 4. Salvar relatório em arquivo
Salva o relatório no arquivo `relatorio_vendas.txt`, criado automaticamente na mesma pasta do projeto.

---

## Regras de cálculo

| Campo        | Cálculo                                              |
|--------------|------------------------------------------------------|
| Valor bruto  | `preço × quantidade`                                 |
| Desconto     | 5% do valor bruto, aplicado se `quantidade > 10`     |
| Valor final  | `valor bruto − desconto`                             |

**Exemplo:** Produto "Camiseta" a R$ 50,00, quantidade 15
- Valor bruto: R$ 750,00
- Desconto (5%): R$ 37,50
- Valor final: R$ 712,50

---

## Exemplo de relatório gerado

```
=== Relatório de Vendas ===

Cliente: João Silva
Produto: Camiseta
Quantidade: 15
Valor Bruto: R$ 750.00
Desconto: R$ 37.50
Valor Final: R$ 712.50

Cliente: Maria Souza
Produto: Notebook
Quantidade: 1
Valor Bruto: R$ 2500.00
Desconto: R$ 0.00
Valor Final: R$ 2500.00

Total arrecadado pela loja: R$ 3212.50
```

---

## Tratamento de erros

- Entradas não numéricas em campos de preço, estoque e quantidade são capturadas com `try-except` e solicitadas novamente.
- Falhas ao salvar o arquivo (ex.: permissão negada) exibem uma mensagem de erro sem encerrar o programa.
- Tentativa de venda sem produtos cadastrados exibe aviso e retorna ao menu.
