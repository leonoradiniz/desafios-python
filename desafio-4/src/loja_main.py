from loja_funcoes import (
    cadastrar_produto,
    realizar_venda,
    gerar_relatorio,
    salvar_relatorio,
)

MENU = """
========== Loja Simples ==========
1. Cadastrar produto
2. Realizar venda
3. Gerar relatório
4. Salvar relatório em arquivo
5. Sair
==================================
Escolha uma opção: """


def main():
    produtos = []
    vendas = []

    while True:
        opcao = input(MENU).strip()

        if opcao == "1":
            produtos = cadastrar_produto(produtos)
            input("Pressione Enter para continuar...")
        elif opcao == "2":
            vendas = realizar_venda(produtos, vendas)
            input("Pressione Enter para continuar...")
        elif opcao == "3":
            gerar_relatorio(vendas)
            input("Pressione Enter para continuar...")
        elif opcao == "4":
            salvar_relatorio(vendas)
            input("Pressione Enter para continuar...")
        elif opcao == "5":
            print("Encerrando o programa. Até logo!")
            break
        else:
            print("Opção inválida. Escolha entre 1 e 5.")


if __name__ == "__main__":
    main()
