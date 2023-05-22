cont = 0
soma = 0
menor = 0
maior = 0
resu = True
num = 0

while resu == True:
    num = int(input(("Digite um numero: ")))
    if cont == 0:
        menor = num
        maior = num
    if num < menor:
        menor = num
    if num > maior:
        maior = num
    soma = soma + num
    cont += 1
    continuar = str(input("""Deseja continuar inserindo valores? (S/N)
    """)).upper()
    if continuar == "S":
        resu = True
    elif continuar == "N":
        resu = False

media = soma / cont

print("A média dos valores digitados foi {}, e o menor numero foi {}, e o maior foi {}".format(media,menor,maior))