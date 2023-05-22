frase = str(input("Digite uma frase/palavra: ")).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''


for letra in range(len(junto)-1,-1,-1):
    inverso = inverso + junto[letra]
# outra opção -> inverso = junto[::-1]

if inverso == junto:
    print("A frase é um palindromo")
else:
    print("A frase não é um palindromo")



