imprimir = str(input("Informe se deseja imprimir um retângulo (s/n): "))

if imprimir == "s": 
    alt = int(input("Informe a altura do retângulo: "))
    larg = int(input("Informe a largura do retângulo: "))
    while alt > larg:
        alt = int(input("Informe a altura do retângulo: "))
        larg = int(input("Informe a largura do retângulo: "))
    
    for a in range(1, alt):
        print(" ")
        for l in range(1, larg):
            print("*", end=" ")
    
    print(" ")