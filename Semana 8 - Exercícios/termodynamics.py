import math

def variacaoEntropia(TIc, TFc):
    TIk = TIc + 273
    TFk = TFc + 273
    VE = 8.314 * math.log(TFk/TIk)
    return VE

qExp = int(input("Informe a quantidade de experimentos: "))
print("")

for i in range(qExp):
    print(f"Experimento {i + 1}:")
    tiC = float(input(". Informe a temperatura inicial (Celsius): "))
    tfC = float(input(". Informe a temperatura final (Celsius): "))

    vE = variacaoEntropia(tiC, tfC)
    print(f". A variação de entropia é {vE:.3f} J/(mol K)")
    print("")