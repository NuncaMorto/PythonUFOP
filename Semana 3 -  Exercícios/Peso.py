h = float(input("Digite a altura: "))
sexo = str(input("Digite o sexo (m ou f): "))

if sexo == "m": 
    sexM = (72.7 * h) - 58
    print(f"O peso ideal é: {sexM:.2f}")
elif sexo == "f": 
    sexF = (62.1 * h) - 44.7
    print(f"O peso ideal é: {sexF:.2f}")