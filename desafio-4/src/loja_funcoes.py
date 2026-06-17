import os

TAXA_DESCONTO = 0.05
LIMITE_DESCONTO = 10


def cadastrar_produto(produtos):
    print("\n--- Cadastrar Produto ---")
    while True:
        nome = input("Nome do produto: ").strip()
        if not nome:
            print("Erro: o nome não pode ser vazio.")
            continue
        if any(p["nome"].lower() == nome.lower() for p in produtos):
            print("Erro: já existe um produto com esse nome!")
            continue
        break

    while True:
        try:
            preco = float(input("Preço (R$): ").replace(",", "."))
            if preco <= 0:
                print("Erro: o preço deve ser maior que zero!")
                continue
            break
        except ValueError:
            print("Erro: insira um número válido para o preço!")

    while True:
        try:
            estoque = int(input("Estoque inicial: "))
            if estoque < 0:
                print("Erro: o estoque não pode ser negativo!")
                continue
            break
        except ValueError:
            print("Erro: insira um número inteiro para o estoque!")

    produtos.append({"nome": nome, "preco": preco, "estoque": estoque})
    print(f"Produto '{nome}' cadastrado com sucesso!")
    return produtos


def listar_produtos(produtos):
    if not produtos:
        print("Nenhum produto cadastrado!")
        return
    print("\n--- Produtos Disponíveis ---")
    for i, p in enumerate(produtos, start=1):
        print(f"{i}. {p['nome']} - R$ {p['preco']:.2f} - Estoque: {p['estoque']}")


def calcular_venda(produto, quantidade):
    valor_bruto = produto["preco"] * quantidade
    desconto = valor_bruto * TAXA_DESCONTO if quantidade > LIMITE_DESCONTO else 0.0
    valor_final = valor_bruto - desconto
    produto["estoque"] -= quantidade
    return {
        "produto": produto["nome"],
        "quantidade": quantidade,
        "valor_bruto": valor_bruto,
        "desconto": desconto,
        "valor_final": valor_final,
    }


def realizar_venda(produtos, vendas):
    print("\n--- Realizar Venda ---")

    if not produtos:
        print("Nenhum produto cadastrado. Cadastre produtos antes de realizar uma venda.")
        return vendas

    while True:
        nome_cliente = input("Nome do cliente: ").strip()
        if nome_cliente:
            break
        print("Erro: o nome do cliente não pode ser vazio!")

    listar_produtos(produtos)

    while True:
        try:
            indice = int(input("Selecione o produto pelo número: ")) - 1
            if indice < 0 or indice >= len(produtos):
                print("Erro: índice inválido!")
                continue
            produto = produtos[indice]
            if produto["estoque"] == 0:
                print("Erro: produto sem estoque disponível.")
                continue
            break
        except ValueError:
            print("Erro: insira um número inteiro.")

    while True:
        try:
            quantidade = int(input(f"Quantidade (disponível: {produto['estoque']}): "))
            if quantidade <= 0:
                print("Erro: a quantidade deve ser maior que zero!")
                continue
            if quantidade > produto["estoque"]:
                print(f"Erro: estoque insuficiente! Disponível: {produto['estoque']}.")
                continue
            break
        except ValueError:
            print("Erro: insira um número inteiro para a quantidade!")

    dados_venda = calcular_venda(produto, quantidade)
    dados_venda["cliente"] = nome_cliente
    vendas.append(dados_venda)

    print(f"\nVenda realizada com sucesso!")
    print(f"Valor bruto:  R$ {dados_venda['valor_bruto']:.2f}")
    print(f"Desconto:     R$ {dados_venda['desconto']:.2f}")
    print(f"Valor final:  R$ {dados_venda['valor_final']:.2f}")
    return vendas


def linhas_relatorio(vendas):
    linhas = ["=== Relatório de Vendas ===\n"]
    if not vendas:
        linhas.append("Nenhuma venda realizada.\n")
        return linhas
    for v in vendas:
        linhas.append(f"Cliente: {v['cliente']}")
        linhas.append(f"Produto: {v['produto']}")
        linhas.append(f"Quantidade: {v['quantidade']}")
        linhas.append(f"Valor Bruto: R$ {v['valor_bruto']:.2f}")
        linhas.append(f"Desconto: R$ {v['desconto']:.2f}")
        linhas.append(f"Valor Final: R$ {v['valor_final']:.2f}")
        linhas.append("")
    total = sum(v["valor_final"] for v in vendas)
    linhas.append(f"Total arrecadado pela loja: R$ {total:.2f}")
    return linhas


def gerar_relatorio(vendas):
    print()
    for linha in linhas_relatorio(vendas):
        print(linha)


def salvar_relatorio(vendas):
    caminho = os.path.join(os.path.dirname(os.path.abspath(__file__)), "relatorio_vendas.txt")
    try:
        with open(caminho, "w", encoding="utf-8") as arquivo:
            for linha in linhas_relatorio(vendas):
                arquivo.write(linha + "\n")
        print(f"Relatório salvo com sucesso em: {caminho}")
    except OSError as e:
        print(f"Erro ao salvar o relatório: {e}")
