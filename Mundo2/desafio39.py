from datetime import date
anoatual = date.today().year
anonasc = int(input("Qual ano de nascimento? "))
idade = anoatual - anonasc
if idade < 0 or anonasc > anoatual:
    print("Digite um ano válido")
elif idade < 18:
    idade = 18 - idade
    print("Voce ainda não precisa se alistar")
    print("Seu alistamento será daqui a {} ano(s)".format(idade))
    print("No ano de {}".format(idade + anoatual))
elif idade > 18:
    idade = idade - 18
    print("Voce deve se alistar")
    print("Seu alistamento deve ter ocorrido há {} ano(s)".format(idade))
    print("No ano de {}".format(anoatual - idade))
elif idade == 18:
    print("Voce deve se alistar no ano atual")





