idade = int(input("Informe a idade de uma pessoa: "))
if idade >= 16:
    print("Essa pessoa pode votar!")
if idade < 16:
    print("Essa pessoa apenas pode votar quando completar 16 anos e tirar a carteira de motorista aos 18 anos!")
elif idade >= 18:
    print("Além de conseguir votar, essa pessoa podera tirar a carteira de motorista!")