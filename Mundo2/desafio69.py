maiordezo = 0
homens = 0
muiemenosvinte = 0

idade = 0



while True:
    idade = int(input("Qual a idade? "))
    sexo = " "
    while sexo not in "MF":
        sexo = str(input("Qual o sexo (M / F)? ")).upper().strip()
    if idade > 18 and sexo == "M":
        homens += 1
        maiordezo += 1
    elif idade <= 18 and sexo == "M":
        homens += 1
    elif idade < 20 and sexo =="F":
        muiemenosvinte += 1
    elif idade > 18 and sexo =="F":
        maiordezo += 1
    continu = " "
    while continu not in "SN":
        continu = str(input("Deseja continuar(S / N)? ")).upper().strip()
    if continu == "N":
        break

print(f"Pessoas maiores que 18 anos -> {maiordezo}, homens registrados -> {homens}, mulheres menores de vinte anos -> {muiemenosvinte}")