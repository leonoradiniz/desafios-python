import funcoes

def main():
    """
    Função principal que orquestra o fluxo do programa, exibe o menu
    e armazena a lista de funcionários cadastrados pelo usuário.
    """
    lista_funcionarios = []

    while True:
        print("\n" + "="*35)
        print("   MENU DE FOLHA DE PAGAMENTO")
        print("="*35)
        print("1. Cadastrar funcionário")
        print("2. Gerar relatório")
        print("3. Salvar relatório em .txt")
        print("4. Sair")
        print("="*35)

        opcao = input("Escolha uma opção (1-4): ").strip()

        match opcao:
            case '1':
                print("\n--- Novo Cadastro ---")
                
                cadastro_funcionario = funcoes.cadastrar_funcionario()
                registro_processado = funcoes.processar_salario(cadastro_funcionario)
                lista_funcionarios.append(registro_processado)

                print(f"\n[Sucesso] Funcionário(a) {registro_processado['nome']} cadastrado(a)!")

            case '2':
                if len(lista_funcionarios) == 0:
                    print("[Aviso] Nenhum funcionário cadastrado ainda. Faça um cadastro primeiro.")
                else:
                    funcoes.gerar_relatorio(lista_funcionarios)

            case '3':
                if len(lista_funcionarios) == 0:
                    print("[Aviso] Nenhum funcionário cadastrado para salvar.")
                else:
                    funcoes.salvar_relatorio(lista_funcionarios)

            case '4':
                print("\nEncerrando o sistema. Até logo!\n")
                break

            case _:
                print("\n[Erro] Opção inválida. Digite um número de 1 a 4.")

if __name__ == "__main__":
    main()