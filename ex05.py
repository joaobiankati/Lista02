num1 = int(input("Informe um número inteiro: "))
num2 = int(input("Informe o segundo número inteiro: "))
num3 = int(input("Informe o terceiro número inteiro: "))
if num1 > num2:
    num1, num2 = num2, num1
if num1 > num3:
    num1, num3 = num3, num1
if num2 > num3:
    num2, num3 = num3, num2

print("A ordem crescente é: ")
print(num1)
print(num2)
print(num3)