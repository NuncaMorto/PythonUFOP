candidato1 = str(input("Forneça o nome do candidato 1: "))
n1 = int(input("Forneça o número do candidato 1: "))
candidato2 = str(input("Forneça o nome do candidato 2: "))
n2 = int(input("Forneça o número do candidato 2: "))

n1Quantidade = 0
n2Quantidade = 0
nInvalido = 0

while True:
    nEleitores = int(input("Forneça a quantidade de eleitores: "))
    if nEleitores >= 3:
        break
    print("A quantidade de eleitores é inferior a 3")

print("## Votação Iniciada")
for i in range(nEleitores):
    voto = int(input("Forneça o número do candidato que deseja votar: "))
    if voto == n1:
        n1Quantidade += 1
    elif voto == n2:
        n2Quantidade += 1
    else:
        nInvalido += 1
print("## Votação Encerrada")

votosValidos = n1Quantidade + n2Quantidade
totalVotos = votosValidos + nInvalido

print(f"\nVotos válidos: {votosValidos / totalVotos * 100:.2f}% ({votosValidos} votos)")
print(f"Votos inválidos: {nInvalido / totalVotos * 100:.2f}% ({nInvalido} votos)")
print(f"Votos para {candidato1}: {n1Quantidade / votosValidos * 100:.2f}% ({n1Quantidade} votos)")
print(f"Votos para {candidato2}: {n2Quantidade / votosValidos * 100:.2f}% ({n2Quantidade} votos)")