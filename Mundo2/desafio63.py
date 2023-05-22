a = 0
b = 1
c = 0
cont = 2
num = int(input("Digite quantos numeros da sequencia deseja ver: "))
if num == 1:
    print(a)
else:
    print(a)
    print(b)
    while cont < num:
        c = a + b
        print(c)
        a = b
        b = c
        cont += 1