menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Qual valor gostaria de despositar: "))
        if valor < 0:
            print("Valor de desposito invalido")
        else:
            saldo = saldo + valor
            extrato += f"Desito: R$ {valor:.2f}\n"
    elif opcao == "s":
        valor_saque = float(input("Qual valor gostaria de sacar: "))
        if valor_saque < 0:
            print("Valor de saque invalido")
        elif numero_saques >= LIMITE_SAQUE:
            print("Quantidade máxima de 3 saques atingido")
        elif valor_saque > saldo:
            print("Conta sem saldo")
        elif valor_saque > limite:
            print("Valor do saque acima do permitido de R$ 500,00")
        else:
            print (f"Favor retirar R${valor_saque} da maquina")
            numero_saques += 1
            aldo = saldo - valor_saque
            extrato += f"Saque: R$ {valor_saque:.2f}\n"
    elif opcao == "e":
        print("\n=========EXTRATO BANCARIO=========")
        print("Nao foram realizadas movimentacoes" if not extrato else extrato)
        print(f"\nSaldo em conta: R$ {saldo:.2f}")
        print("===================================")
    elif opcao == "q":
        print("Obrigado por usar nosso banco")
        break
    else:
        print("Operacao invalida, selecine uma operacao valida")


