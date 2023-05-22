barato = ''
maismil = 0
total = 0
menorp = 0
cont = 0


while True:
    nome = str(input("Qual o nome do produto? "))
    preco = float(input("Qual o preço? "))
    cont += 1
    if preco > 1000:
        maismil += 1
    if cont == 1 or preco < menorp:
        menorp = preco
        barato = nome
    '''else:
       if preco < menorp:
        menorp = preco
        barato = nome'''
    total = total + preco
    continu = " "
    while continu not in "SN":
        continu = str(input("Deseja continuar(S / N)? ")).upper().strip()
    if continu == "N":
        break
print(f"O total gasto foi {total}, {maismil} produto(s) custam mais que mil e produto mais barato foi {barato}")

