while True:
    imprimir = str(input("Informe se deseja imprimir um retângulo (s/n): "))

    if imprimir == "n":
        break

    if imprimir == "s":
        alt = int(input("Informe a altura do retângulo: "))
        larg = int(input("Informe a largura do retângulo: "))

        while alt <= 0 or larg <= 0 or larg <= alt:
            print("Entrada inválida.")
            alt = int(input("Informe a altura do retângulo: "))
            larg = int(input("Informe a largura do retângulo: "))

        for a in range(alt):
            for l in range(larg):
                print("*", end="")
            print()