PT1 = float(input("Informe a nota PT1: "))
EP1 = float(input("Informe a nota EP1: "))
PT2 = float(input("Informe a nota PT2: "))
EP2 = float(input("Informe a nota EP2: "))

AV1 = 0.4 * PT1 + 0.1 * EP1
AV2 = 0.4 * PT2 + 0.1 * EP2
NS = AV1 + AV2

print(f"A nota na AV1 é: {AV1:.2f}")
print(f"A nota na AV2 é: {AV2:.2f}")

print(f"A nota no semestre é: {NS:.2f}")


