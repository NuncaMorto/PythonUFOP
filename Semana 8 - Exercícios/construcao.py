import math

def imprime(tTijolo, qTijolo, qArgamassa):
    print(f". O tipo de tijolo é: {tTijolo}")
    print(f". A quantidade de tijolos é: {math.ceil(qTijolo)}")
    print(f". A quantidade de argamassa é: {math.ceil(qArgamassa)}")

def calculosParede(Lp, Hp):
    Ap = Lp * Hp
    if Ap <= 60000:
        At = 171
        G = 1000
        tTijolo = "A"
    elif Ap <= 90000:
        At = 200
        G = 1200
        tTijolo = "B"
    else:
        At = 300
        G = 1400
        tTijolo = "C"
    
    qTijolos = Ap / At
    qArgamassa = Ap / G
    return tTijolo, math.ceil(qTijolos), math.ceil(qArgamassa)

def main():
    while True:
        lParede = float(input("Defina a largura da parede (cm): "))
        aParede = float(input("Defina a altura da parede (cm): "))
        
        if lParede <= 0 or aParede <= 0:
            break
        
        tTijolo, qTijolos, qArgamassa = calculosParede(lParede, aParede)
        imprime(tTijolo, qTijolos, qArgamassa)
        print("")

if __name__ == "__main__":
    main()
