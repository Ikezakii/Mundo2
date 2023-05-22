'''term = int(input("Digite o primeiro termo: "))
raz = int(input("Digite a razão da progrssão: "))
print(term)
for i in range(9):
    term = term + raz
    print(term)'''
term = int(input("Digite o primeiro termo: "))
raz = int(input("Digite a razão da progrssão: "))
cont = 0
op = 1
print(term)
while cont < 10:
    term = term + raz
    print(term)
    cont += 1
while op != 0:
    op = int(input("Deseja mostrar quantos termos mais? "))
    for i in range(op):
        term = term + raz
        print(term)