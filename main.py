pedido = []

pratos_principais = [
    ("Bruschetta", 18.00),
    ("Salada Caprese", 22.00),
    ("Parmegiana", 35.90),
    ("Macarrão a Bolonhesa", 30.00),
    ("Frango Grelhado", 32.00),
    ("Peixe Assado", 42.00)
]

acompanhamentos = [
    ("Arroz", 15.00),
    ("Batata Frita G", 15.00),
    ("Salada", 15.00),
]

bebidas = [
    ("Suco", 10.00),
    ("Refrigerante 1L", 10.00),
    ("Agua", 10.00),
]

sobremesas = [
    ("Pudim", 15.00),
    ("Brigadeiro", 10.00),
    ("Sorvete", 10.00)
]

def mostrar_categorias(titulo, pratos):
    print(f"--- {titulo} ---")
    for numero, (nome, preco) in enumerate(pratos, start=1):
            print(f"{numero} - {nome} | R${preco:.2f}")

def mostrar_menu():
     print("------------------------------------------")
     print("            MENU PRINCIPAL ")
     print("------------------------------------------")
     print(
          "\n 1 - Ver Cardápio"
          "\n 2 - Fazer Pedido"
          "\n 3 - Ver Pedido e total"
          "\n 4 - Finalizar Pedido"
          "\n 5 - Sair"
     )

def finalizar_pedido(pedido):
    if not pedido:
        print("O Pedido está vazio")
        return

    total = 0
    print("--- RESUMO DO PEDIDO ---")

    for nome, preco in pedido:
        print(f"{nome} | R${preco:.2f}")
        total += preco

    print(f"Total: R${total:.2f}")



while True:
    mostrar_menu()
    acao = int(input("-> "))

    if acao == 1:
        mostrar_categorias("PRATOS PRINCIPAIS", pratos_principais)
        mostrar_categorias("ACOMPANHAMENTOS", acompanhamentos)
        mostrar_categorias("BEBIDAS", bebidas)
        mostrar_categorias("SOBREMESAS", sobremesas)

    elif acao == 2:
        todos_pratos = (
            pratos_principais
            + acompanhamentos
            + bebidas
            + sobremesas
        )
        while True:
            encontrado = None
            item = input("Nome do Prato: ").lower().strip().replace(" ", "")

            for nome_prato, preco in todos_pratos:
                nome_normalizado = nome_prato.lower().replace(" ", "")

                if nome_normalizado == item:
                    encontrado = (nome_prato, preco)
                    break

            if encontrado:
                pedido.append(encontrado)
                print("Pedido Adicionado.")
            else:
                print("Prato Não Encontrado.")

            continuar = input("Deseja mais alguma coisa? [s/n]").lower().strip()

            if continuar == "n":
                break

    elif acao == 3:
        print("----------------------------------------------")
        print("                SEU PEDIDO                              ")
        print("----------------------------------------------")

        for comida in pedido:
            print(f"Item: {comida} | R${preco:.2f}")
        total = 0
        for nome, preco in pedido:
            total += preco

        print(f"Valor total: R${total:.2f}")

    elif acao == 4:
        finalizar_pedido(pedido)

    elif acao == 5:
        print("Saindo do Sistema...")
        break


    else:
        print("Erro, Digite o número da opção.")