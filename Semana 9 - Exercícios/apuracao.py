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

nomeCandidatos = inputVetor("Digite os nomes dos candidatos: ", str)
votos = inputVetor("Digite as quantidades de votos: ", int)

if len(nomeCandidatos) < 3:
    print("Quantidade de candidatos insuficiente")
elif len(nomeCandidatos) != len(votos):
    print("Vetores com tamanhos diferentes")
else:
    maiorV = votos[0]
    maiorQ = nomeCandidatos[0]
    for i in range(1, len(nomeCandidatos)):
        if votos[i] > maiorV:
            maiorV = votos[i]
            maiorQ = nomeCandidatos[i]
    print(f"Vencedor das eleições: {maiorQ}")