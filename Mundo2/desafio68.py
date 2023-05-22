from random import randint

vitcpu = 0
vitplay = 0
resul = 0
while vitcpu == 0:
    numplay = int(input("Qual numero deseja jogar (0 a 10): "))
    numcpu = randint(1,10)
    escplay = str(input("Impar ou Par (I / P)? ")).upper()
    if escplay == "P":
        esccpu = "I"
        resul = (numplay + numcpu) % 2
        if resul == 0:
            vitplay += 1
        else:
            vitcpu += 1
    elif escplay == "I":
        esccpu = "P"
        resul = (numplay + numcpu) % 2
        if resul > 0:
            vitplay += 1
        else:
            vitcpu += 1
print(f"O jogo acabou, o jogador fez {vitplay} vitorias")
