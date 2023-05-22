gen = ""

while gen != "F" and "M":
    gen = str(input("Digite o sexo da pessoa (F/M): ")).upper()
    if gen != "F" and "M":
        print("Digite um valor válido")