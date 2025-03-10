def estatNotas(vetor):
    maiorNota = vetor[0]
    menorNota = vetor[0]
    mediaNota = vetor[0]

    for i in range(len(vetor)):
        if vetor[i] > maiorNota:
            maiorNota = vetor[i]
        if vetor[i] < menorNota:
            menorNota = vetor[i]
        mediaNota += vetor[i]
    
    mediaNota = mediaNota / len(vetor)
    return maiorNota, menorNota, mediaNota

def acimaValor(vetor, mediaCorte):
    acimaMedia = [ ]
    indice = [ ]
    for i in range(len(vetor)):
        if vetor[i] > mediaCorte:
            acimaMedia.append(vetor[i])
            indice.append(i)
    return acimaMedia, indice

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

    maiorNota, menorNota, mediaNota = estatNotas(notas)

    print(f"Maior nota: {maiorNota:.1f}")
    print(f"Menor nota: {menorNota:.1f}")
    print(f"Nota média: {mediaNota:.1f}")

    acimaMedia, indice = acimaValor(notas, mediaNota)

    print(f"Notas acima da média:")
    for i in range(len(acimaMedia)):
        print(f" - [{indice[i]}] = {acimaMedia[i]:.1f}")

main()