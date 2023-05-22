from datetime import date
maior = []
menor = []
for i in range(7):
    nasc = int(input("Qual ano de nascimento? "))
    if date.today().year - nasc >= 18:
        maior.append(nasc)
    elif date.today().year - nasc < 18:
        menor.append(nasc)
print("{} pessoas são maior de idade e {} pessoas são menor de idade".format(len(maior),len(menor)))
print("Essas são as datas dos maiores de idade")
for i in range(len(maior)):
    print(maior[i])
print("Essas são as datas dos menores de idade")
for i in range(len(menor)):
    print(maior[i])
