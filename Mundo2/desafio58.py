import random

tentativas = 0
resp = 0
num = random.randint(0,10)




while resp != num:
        resp = int(input("Digite o numero que voce acha correto: "))
        if(resp != num):
            print("Voce errou, o numero não era {0}".format(resp))
        tentativas +=1

print("Voce levou {} tentativas para acertar".format(tentativas))