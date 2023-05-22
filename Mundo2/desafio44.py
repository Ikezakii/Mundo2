preco = float(input("Digite o preço do produto: R$"))
escolha = int(input("""Escolha a opção de pagamento
    1 - a vista no cartao (5% desconto)
    2 - a vista no dinheiro(10% desconto)
    3 - 2x no cartão
    4 - 3x ou mais no cartão(20% juros)
    """))

if escolha == 1:
     desconto = preco * (5/100)
     preco = preco - desconto
     print("Voce irá pagar R${:.2f}".format(preco))
elif escolha == 2:
     desconto = preco * (10 / 100)
     preco = preco - desconto
     print("Voce irá pagar R${:.2f}".format(preco))
elif escolha == 3:
     preco = preco/2
     print("Voce irá pagar duas parelas de R${:.2f}".format(preco))
elif escolha == 4:
     vezes = int(input("Quantas vezes no cartão? "))
     juros = preco * (20/100)
     preco = (preco + juros) / vezes
     print("Voce irá pagar {} parcelas de R${:.2f}".format(vezes, preco))
else:
     print("Opção inválida")







