lista = []
total = 0
qtd = int(input("Quantos numeros deseja inserir? "))

for i in range(qtd):
 n = float(input("Digite um número: "))
 lista.append(n)
 total = total + n


media = total / len(lista)

print("A média é {0}".format(media))

if media > 7:
    print("Parabéns, voce está aprovado")
elif media == 7:
    print("Passou de raspão")
elif media < 7:
    print("Estude mais e se prepare para recuperação")
