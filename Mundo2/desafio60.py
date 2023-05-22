num = int(input("Digite um numero: "))
fat = num - 1
while fat != 0:
 print("{} x {} = {}".format(num,fat, num*fat))
 num = num * fat
 fat -= 1
print(num)