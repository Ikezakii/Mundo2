idadesom = 0
maioridadehom = 0
nomemaiorh = ''
idademenorf = 0


for i in range(4):
    print("----{} pessoa----".format(i+1))
    nome = str(input("Digiteo nome da pessoa: ")).strip()
    idade = int(input("Digite a idade da pessoa: "))
    sexo = str(input("Digite a idade da pessoa (M/F): ")).strip().upper()
    idadesom = idadesom + idade
    if i == 0 and sexo == "M":
        maioridadehom = idade
        nomemaior = nome
    if sexo == "M" and idade > maioridadehom:
        maioridadehom = idade
        nomemaiorh = nome
    if sexo == "F" and idade < 20:
        idademenorf = idademenorf + 1


idademed = idadesom / 4
print("A media de idade do grupo é {}".format(idademed))
print("O homem mais velho é {} com {} anos".format(nomemaiorh, maioridadehom))
print("A quantidade de mulheres com menos de 20 anos é {}".format(idademenorf))
