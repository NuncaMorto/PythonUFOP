import math


tipo = int(input("Forneça o tipo de ladrilho (1 ou 2): "))
areaS = int(input("Forneça a área da sala: "))

if tipo == 1: 
    areaS = areaS / 80
    print(f"Quantidade de ladrilhos: {math.ceil(areaS)}")
elif tipo == 2: 
    areaS = areaS / 60
    print(f"Quantidade de ladrilhos: {math.ceil(areaS)}")
