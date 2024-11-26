a1 = float(input("Informe o primeiro termo: "))
q = float(input("Informe a razão: "))
n = int(input("Informe o número do termo: "))

an = a1 * q ** (n - 1)

formatted = "{:.2f}".format(an)

print(f"O termo a({round(n, 0)}) é {formatted}")