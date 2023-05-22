'''pesos = []
for i in range(5):
    peso = int(input("Digite o peso da pessoa: "))
    pesos.append(peso)

pesoscre = sorted(pesos)

print("Maior peso {} e menor peso {}".format(pesoscre[4],pesoscre[0]))'''
maior = 0
menor = 0

for i in range(5):
    peso = int(input("Digite o peso da pessoa: "))
    if i == 0:
        maior = peso
        menor = peso
    else:
     if peso > maior:
        maior = peso
     elif peso < menor:
        menor = peso
print("Maior peso {} e menor peso {}".format(maior,menor))