from datetime import date
anoatual = date.today().year
anonasc = int(input("Qual ano de nascimento? "))
idade = anoatual - anonasc

if idade < 0 or anonasc > anoatual:
    print("Digite um ano válido")
elif idade <= 9:
    print(idade)
    print("Classificação: MIRIM")
elif idade <= 14:
    print(idade)
    print("Classificação: INFANTIL")
elif idade <= 19:
    print(idade)
    print("Classificação: JUNIOR")
elif idade<= 25:
    print(idade)
    print("Classificação: SENIOR")
else:
    print(idade)
    print("Classificação: MASTER")





