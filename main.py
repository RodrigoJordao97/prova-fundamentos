total_vendas = 0
total_bruto = 0
total_descontos = 0
total_liquido = 0

while True:
    print("SISTEMA DE VENDAS")
    print("1 - Registrar venda")
    print("2 - Ver resumo parcial")
    print("3 - Encerrar Sstema")

    opcao = input("Escolha uma opção:")

    if opcao == "1":
        produto = input("Nome do produto:")

        valor_produto = float(input("Valor do produto: "))
        quantidade = int(input("Quantidade: "))

        valor_bruto = valor_produto * quantidade

#Desconto

        if valor_bruto >= 1000:
            desconto_percentual = 15
        else:
            desconto_percentual = 10

        valor_desconto = valor_bruto * (desconto_percentual / 100)
        valor_final = valor_bruto - valor_desconto

#Total

        total_vendas += 1
        total_bruto += valor_bruto
        total_descontos += valor_desconto
        total_liquido += valor_final

        print(f"Valor Bruto da venda: R${ valor_bruto:.2f} ")
        print(f"Desconto aplicado: {desconto_percentual}%")
        print(f"Valor do desconto: R$ {valor_desconto:.2f}")
        print(f"Valor final da venda: R$ {valor_final:.2f}")
        print("Venda registrada com sucesso!")
    
    elif opcao == "2":
        print("RESUMO PARCIAL")
        print(f"Total de vendas realizadas: {total_vendas}")
        print(f"Total bruto vendido: R$ {total_bruto:.2f}")
        print(f"Total de descontos concedidos: R$ {total_descontos:.2f}")
        print(f"Total líquido vendido: R$ {total_liquido:.2f}")

    elif opcao == "3":
        print("RESUMO FINAL")
        print(f"Total de vendas realizadas: {total_vendas}")
        print(f"Total bruto vendido: R$ {total_bruto:.2f}")
        print(f"Total de descontos concedidos: R$ {total_descontos:.2f}")
        print(f"Total líquido vendido: R$ {total_liquido:.2f}")

        print("Sistema encerrado.")
        break

    else:
        print("Opção inválida! Tente novamente.")