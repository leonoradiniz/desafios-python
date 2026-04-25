def calcular_salario_estagiario(salario_bruto):
    """
    Retorna o salário líquido de um estagiário e seus descontos.
    Como não há descontos, os valores de INSS e IRRF são retornados como zero.
    """
    salario_liquido = salario_bruto 
    inss = 0.0
    irrf = 0.0
    
    return salario_liquido, inss, irrf


def calcular_salario_clt(salario_bruto):
    """
    Calcula o salário líquido, o desconto de INSS e o desconto de IRRF 
    de um funcionário CLT com base em seu salário bruto.
    """
    inss = salario_bruto * 0.08
    salario_liquido = salario_bruto - inss
    
    irrf = 0.0
    if salario_bruto > 2000.00:
        irrf = salario_liquido * 0.10
        salario_liquido -= irrf
    else:
        pass
        
    return salario_liquido, inss, irrf


def calcular_salario_freelancer(valor_hora, horas_trabalhadas):
    """
    Calcula o salário líquido, o desconto fixo (mapeado como INSS) 
    e o IRRF (zero) de um freelancer, com base em seu salário bruto.
    """
    salario_bruto = valor_hora * horas_trabalhadas
    inss = salario_bruto * 0.05
    irrf = 0.0
    salario_liquido = salario_bruto - inss
    
    return salario_liquido, inss, irrf


def cadastrar_funcionario():
    """
    Solicita os dados de um funcionário via terminal, aplica regras 
    de validação através de laços while, e retorna um dicionário com as informações coletadas.Se algum dos dados for inserido de forma inválida, o laço while retorna para reinserção do dado.
    """
    funcionario = {}

    while True:
        nome_funcionario = input("Digite o nome do funcionário: ").strip() 

        if nome_funcionario:
            funcionario['nome'] = nome_funcionario
            break
        else:
            print("Erro: O nome não pode ser vazio. Digite novamente.")


    tipos_funcionario = ["estagiario", "clt", "freelancer"]

    while True:
        tipo_funcionario = input("Digite o tipo de vínculo (estagiario, clt, freelancer): ").strip().lower()

        if tipo_funcionario in tipos_funcionario:
            funcionario['tipo'] = tipo_funcionario
            break
        else:
            print("Erro: Tipo de funcionário inválido. Digite novamente.")


    if tipo_funcionario in ["estagiario", "clt"]:
        while True:
            try:
                salario = float(input(f"Digite o salário bruto do {tipo_funcionario}: "))

                if salario > 0:
                    funcionario['salario_bruto'] = salario
                    break
                else:
                    print("Erro: O salário deve ser maior que zero. Digite novamente.")
            except ValueError:
                print("Erro: Entrada inválida. Digite somente números. Tente novamente.")


    elif tipo_funcionario == "freelancer":
        while True:
            try:
                valor_hora = float(input("Digite o valor por hora: "))

                if valor_hora > 0:
                    funcionario['valor_hora'] = valor_hora
                    break
                else:
                    print("Erro: O valor por hora deve ser maior que zero. Tente novamente.")
            except ValueError:
                print("Erro: Entrada inválida. Digite somente números. Tente novamente.")

        while True:
            try:
                horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas: "))
                if horas_trabalhadas > 0:
                    funcionario['horas_trabalhadas'] = horas_trabalhadas
                    break
                else:
                    print("Erro: A quantidade de horas deve ser maior que zero. Tente novamente.")
            except ValueError:
                print("Erro: Entrada inválida. Digite somente números. Tente novamente.")

    return funcionario


def processar_salario(funcionario):
    """
    Processa os dados de um funcionário para calcular seu salário líquido e impostos separados, e assim retorna um registro com os devidos dados do funcionário.

    Para isso, identifica o tipo de vínculo do funcionário cadastrado no dicionário,
    chama a função de cálculo apropriada para calcular seu salário líquido + descontos (a partir do salário bruto), e estrutura o resultado final.
    """
    tipo_funcionario = funcionario['tipo']
    
    registro_funcionario = {
        'nome': funcionario['nome'],
        'tipo': tipo_funcionario,
        'salario_bruto': 0.0,
        'inss': 0.0,
        'irrf': 0.0,
        'salario_liquido': 0.0
    }

    if tipo_funcionario == "estagiario":
        salario_bruto = funcionario['salario_bruto']
        salario_liquido, inss, irrf = calcular_salario_estagiario(salario_bruto)
        
        registro_funcionario.update({
            'salario_bruto': salario_bruto,
            'inss': inss,
            'irrf': irrf,
            'salario_liquido': salario_liquido
        })
        
    elif tipo_funcionario == "clt":
        salario_bruto = funcionario['salario_bruto']
        salario_liquido, inss, irrf = calcular_salario_clt(salario_bruto)
        
        registro_funcionario.update({
            'salario_bruto': salario_bruto,
            'inss': inss,
            'irrf': irrf,
            'salario_liquido': salario_liquido
        })
        
    elif tipo_funcionario == "freelancer":
        valor_hora = funcionario['valor_hora']
        horas_trabalhadas = funcionario['horas_trabalhadas']
        
        salario_bruto = valor_hora * horas_trabalhadas
        salario_liquido, inss, irrf = calcular_salario_freelancer(valor_hora, horas_trabalhadas)
        
        registro_funcionario.update({
            'salario_bruto': salario_bruto,
            'inss': inss,
            'irrf': irrf,
            'salario_liquido': salario_liquido
        })

    return registro_funcionario


def gerar_relatorio(lista_funcionarios):
    """
    Exibe um relatório formatado no console com os dados de folha de pagamento 
    de todos os funcionários registrados na lista e calcula o total geral pago pela empresa.

    Args:
        lista_funcionarios (list): Lista contendo os dicionários de registros dos funcionários cujos dados foram inseridos pelo usuário.
    """
    print("=== Relatório de Folha de Pagamento ===")

    total_pago = 0.0
    
    for funcionario in lista_funcionarios:

        tipo_inserido = funcionario['tipo']
        if tipo_inserido == "clt":
            tipo_formatado = tipo_inserido.upper()
        elif tipo_inserido == "estagiario" or tipo_inserido == "freelancer":
            tipo_formatado = tipo_inserido.capitalize()
        
        print(f"Nome: {funcionario['nome']}")
        print(f"Tipo: {tipo_formatado}")
        print(f"Salário Bruto: R$ {funcionario['salario_bruto']:.2f}")
        print(f"Desconto INSS: R$ {funcionario['inss']:.2f}")
        print(f"Desconto IRRF: R$ {funcionario['irrf']:.2f}")
        print(f"Salário Líquido: R$ {funcionario['salario_liquido']:.2f}")
        print("-" * 30)
        
        total_pago += funcionario['salario_liquido']

    print(f"Total pago pela empresa: R$ {total_pago:.2f}")


def salvar_relatorio(lista_funcionarios):
    """
    Gera e salva o relatório de folha de pagamento em um arquivo de texto (.txt).

    Args:
        lista_funcionarios (list): Lista contendo os dicionários de registros dos funcionários cujos dados foram inseridos pelo usuário.
    """

    linhas_relatorio = ["=== Relatório de Folha de Pagamento ==="]
    total_pago = 0.0

    for funcionario in lista_funcionarios:
        tipo_inserido = funcionario['tipo']
        
        if tipo_inserido == "clt":
            tipo_formatado = tipo_inserido.upper()
        else:
            tipo_formatado = tipo_inserido.capitalize()
        
        linhas_relatorio.append(f"Nome: {funcionario['nome']}")
        linhas_relatorio.append(f"Tipo: {tipo_formatado}")
        linhas_relatorio.append(f"Salário Bruto: R$ {funcionario['salario_bruto']:.2f}")
        linhas_relatorio.append(f"Desconto INSS: R$ {funcionario['inss']:.2f}")
        linhas_relatorio.append(f"Desconto IRRF: R$ {funcionario['irrf']:.2f}")
        linhas_relatorio.append(f"Salário Líquido: R$ {funcionario['salario_liquido']:.2f}")
        linhas_relatorio.append("-" * 30)
        
        total_pago += funcionario['salario_liquido']

    linhas_relatorio.append(f"Total pago pela empresa: R$ {total_pago:.2f}")

    relatorio_completo = "\n".join(linhas_relatorio)
    # aqui a junção das linhas vem sempre com quebra de linha, para formatação do arquivo
    
    nome_arquivo_relatorio = "relatorio_folha_pgto.txt"

    try:
        with open(nome_arquivo_relatorio, 'w', encoding='utf-8') as arquivo:
            arquivo.write(relatorio_completo)
            
        print(f"Sucesso: Relatório salvo com sucesso no arquivo '{nome_arquivo_relatorio}'.")
        
    except PermissionError:
        print(f"Erro de Permissão: O sistema bloqueou a gravação do arquivo '{nome_arquivo_relatorio}'. Verifique os direitos de administrador da pasta atual.")

    except IOError as e:
        print(f"Erro de Entrada/Saída: Houve um problema físico ou de sistema ao salvar o arquivo. Detalhes: {e}")
        
    except Exception as e:
        print(f"Erro inesperado ao tentar salvar o arquivo: {e}")