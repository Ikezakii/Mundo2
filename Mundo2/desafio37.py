def menu():
 while True:
        try:
            print("-------------------------------------")
            escolha = int(input("""Digite qual tipo de conversão você deseja:
1 - Binário
2 - Octal
3 - Hexadecimal
- Pressione qualquer outra tecla para sair -
Qual será a opção? """))
            if escolha in [1, 2, 3]:
                return escolha
            else:
                exit()
        except ValueError:
            exit()


def resultado():
    while True:
        try:
            num = int(input("Digite o número que deseja ser convertido: "))
            break
        except ValueError:
            print("Digite um número inteiro válido.")

    numesc = menu()

    if numesc == 1:
        num = bin(num)
        print(num)
        print("-------------------------------------")
    elif numesc == 2:
        num = oct(num)
        print(num)
        print("-------------------------------------")
    elif numesc == 3:
        num = hex(num)
        print(num)
        print("-------------------------------------")
    resultado()

resultado()


