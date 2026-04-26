# 🗃️ Sistema de Folha de Pagamento

Um sistema simples desenvolvido em Python para gerenciar o cadastro de funcionários, processar cálculos salariais com base no tipo de vínculo do funcionário e gerar relatórios detalhados tanto no terminal quanto em arquivos `.txt`.

## Funcionalidades

- **Cadastro de Funcionários:** Recebe dados via terminal, com validação de entradas, para três tipos de vínculos de funcionários:
  - **CLT:** Cálculo automático de descontos de INSS (8%) e IRRF (10% para salários acima de R$ 2000,00).
  - **Estagiário:** Registro de salário bruto sem descontos.
  - **Freelancer:** Cálculo baseado em horas trabalhadas e valor da hora, com taxa de desconto fixo de 5%.
- **Geração de Relatórios:** Exibe o detalhamento do salário bruto, descontos e salário líquido de cada funcionário cadastrado, além do total geral pago pela empresa.
- **Exportação de Dados:** Permite salvar o relatório idêntico ao do terminal em um arquivo `.txt` (`relatorio_folha_pgto.txt`) localmente de forma automatizada.

## 📂 Estrutura do Projeto

O projeto é dividido em dois arquivos principais para manter a separação de responsabilidades:

- `funcoes.py`: Contém as funções que modularizam as ações do programa, incluindo a coleta de dados, cálculos matemáticos e a formatação do texto do relatório.
- `main.py`: É o arquivo orquestrador do programa, roda o menu interativo e gerencia o cadastro dos funcionários, geração e salvamento de relatórios, por meio das funções.

## 📌 Pré-requisitos

- **Python 3.10 ou superior:** O projeto utiliza a estrutura condicional `match-case`, que foi introduzida na versão 3.10 da linguagem.

## ▶️ Como Executar

1. Clone ou faça o download deste repositório/arquivos para a sua máquina.
2. Abra o terminal e navegue até a pasta onde os arquivos foram salvos.
3. Execute o comando principal:

`python main.py`
