def estatNotas(vetor):
    maiorNota = vetor[0]
    menorNota = vetor[0]
    mediaNota = 0

    for i in range(len(vetor)):
        if vetor[i] > maiorNota:
            maiorNota = vetor[i]
        if vetor[i] < menorNota:
            menorNota = vetor[i]
        mediaNota += vetor[i]
    
    mediaNota = mediaNota / len(vetor)
    return maiorNota, menorNota, mediaNota

def inputVetor(mensagem, conversao):
    valores = input(mensagem)
    resultado = []
    if valores == '':
        return resultado
    valores = valores.split(',')
    for i in range(len(valores)):
        valor = conversao(valores[i].strip())
        resultado.append(valor)
    return resultado

def main():
    notas = inputVetor("Digite as notas: ", float)

    if not notas:
        print("Nenhuma nota informada")
        return

    maiorNota, menorNota, mediaNota = estatNotas(notas)

    print(f"Maior nota: {maiorNota:.1f}")
    print(f"Menor nota: {menorNota:.1f}")
    print(f"Nota média: {mediaNota:.1f}")

if __name__ == "__main__":
    main()