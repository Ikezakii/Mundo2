r1 = float(input("Digite a reta do triangulo: "))
r2 = float(input("Digite a reta do triangulo: "))
r3 = float(input("Digite a reta do triangulo: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("É possivel fazer um triangulo")
    if r1 == r2 == r3:
        print("Forma um triangulo equilátero")
    elif r1 != r2 != r3:
        print("Forma uma trinagulo escaleno")
    else:
        print("Forma um triangulo isósceles")
else:
    print("Não é possivel fazer um triangulo")
