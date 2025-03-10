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

def acimaValor(vetor, mediaCorte, nomes):
    acimaMedia = []
    indice = []
    listaNomes = []
    for i in range(len(vetor)):
        if vetor[i] > mediaCorte:
            acimaMedia.append(vetor[i])
            indice.append(i)
            listaNomes.append(nomes[i])
    return acimaMedia, indice, listaNomes

def exameEspecial(vetor, nomes):
    abaixoMedia = []
    indice2 = []
    listaNomes = []
    for i in range(len(vetor)):
        if 3 <= vetor[i] < 6:
            abaixoMedia.append(vetor[i])
            indice2.append(i)
            listaNomes.append(nomes[i])
    return abaixoMedia, indice2, listaNomes

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
    nomes = inputVetor("Digite os nomes: ", str)

    if not notas or not nomes or len(notas) != len(nomes):
        print("Dados inválidos")
        return

    maiorNota, menorNota, mediaNota = estatNotas(notas)

    print(f"Maior nota: {maiorNota:.1f}")
    print(f"Menor nota: {menorNota:.1f}")
    print(f"Nota média: {mediaNota:.1f}")

    acimaMedia, indice, lista = acimaValor(notas, mediaNota, nomes)
    print(f"Notas acima da média:")
    for i in range(len(acimaMedia)):
        print(f" - [{indice[i]}] = {acimaMedia[i]:.1f} ({lista[i]})")
    
    abaixoMedia, indice2, lista2 = exameEspecial(notas, nomes)
    print(f"Notas em Exame Especial:")
    for i in range(len(abaixoMedia)):
        print(f" - [{indice2[i]}] = {abaixoMedia[i]:.1f} ({lista2[i]})")

if __name__ == "__main__":
    main()