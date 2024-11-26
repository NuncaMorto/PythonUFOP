p = float(input("Informe o capital inicial: "))
i = float(input("Informe a taxa de juros anual (em %): "))
n = float(input("Informe o número de anos: "))

m = p * (1 + i/100)**n

print(f"O montante final é: {m:.2f}")