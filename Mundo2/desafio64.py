cont = 0
num = 0
soma = 0

while num != 999:
    num = int(input("Digite um número: "))
    if num == 999:
        break
    soma = soma + num
    cont += 1

print("Voce digitou numeros {} vezes e a soma deles é {}".format(cont, soma))