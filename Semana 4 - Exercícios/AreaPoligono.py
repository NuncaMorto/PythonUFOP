import math

qLados = int(input("Digite a quantidade de lados: "))

if qLados < 3:
    print("Não é um polígono")
elif qLados > 6: 
    print("Polígono não identificado")
else:
    mLados = float(input("Digite a medida do lado: "))

    if qLados == 3:
        A = ((mLados ** 2) * math.sqrt(3)) / 4
        print(f"O polígono é um triângulo com área: {A:.2f}")
    elif qLados == 4:
        A = mLados ** 2
        print(f"O polígono é um quadrado com área: {A:.2f}")
    elif qLados == 5:
        A = (5 * mLados ** 2) / (4 * math.tan(0.6283))
        print(f"O polígono é um pentágono com área: {A:.2f}")
    elif qLados == 6:
        A = (3 * (mLados ** 2) * math.sqrt(3)) / 2
        print(f"O polígono é um hexágono com área: {A:.2f}")

    