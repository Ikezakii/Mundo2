escolha = 0
while escolha != 5:
 escolha = int(input("""Qual operação deseja realizar)
              1 - soma
              2 - subtração
              3 - divisão
              4 - multiplicação
              5 - sair do programa
              """))
 if escolha == 1:
    num1 = float(input("Digite o primeiro numero: "))
    num2 = float(input("Digite o segundo numero: "))
    print(num1 + num2)
 if escolha == 2:
    num1 = float(input("Digite o primeiro numero: "))
    num2 = float(input("Digite o segundo numero: "))
    print(num1 - num2)
 if escolha == 3:
    num1 = float(input("Digite o primeiro numero: "))
    num2 = float(input("Digite o segundo numero: "))
    print(num1 / num2)
 if escolha == 4:
    num1 = float(input("Digite o primeiro numero: "))
    num2 = float(input("Digite o segundo numero: "))
    print(num1 * num2)

