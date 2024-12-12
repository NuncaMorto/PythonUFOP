import math

fatorial = int(input("Informe o número que deseja calcular o Fatorial: "))
while fatorial <= 0:
    fatorial = int(input("Número inválido, defina outro: "))
print(f"O Fatorial de {fatorial} é: {math.factorial(fatorial)}")