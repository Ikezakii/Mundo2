num = 0
while num >= 0:
    num = int(input("Qual tabuada deseja ver? "))
    if num < 0 :
        break
    for i in range(11):
        print(f"{num} x {i} = {num*i}")