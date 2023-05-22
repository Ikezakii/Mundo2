from math import sqrt

nprim = False
prim = False


num =int(input("Digite um numero: "))
if num <= 1:
    print("O numero não é primo")
    exit()

raiz = round(sqrt(num))
for i in range(2,raiz+1):
 if num % i == 0:
  nprim = True
 else:
  prim = True

if nprim == True:
  print("O numero não é primo")
elif prim == True:
  print("O numero é primo")