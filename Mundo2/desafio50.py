total = 0
for i in range(1,7):
     num = int(input("Digite um numero: "))
     if num % 2 == 0:
         total = total + num
print(total)