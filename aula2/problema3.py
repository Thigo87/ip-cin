num1 = int(input("Digite um valor inteiro: "))
num2 = int(input("Digite um valor inteiro: "))

if num1 > num2:
  num1, num2 = num2, num1

print(f"Valor de num1: {num1} e valor de num2: {num2}")