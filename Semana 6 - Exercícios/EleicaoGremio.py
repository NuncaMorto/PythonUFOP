candidato1 = str(input("Forneça o nome do candidato 1: "))
n1 = int(input("Forneça o número do candidato 1: "))
candidato2 = str(input("Forneça o nome do candidato 2: "))
n2 = int(input("Forneça o número do candidato 2: "))

n1Quantidade = 0
n2Quantidade = 0
nInvalido = 0

nEleitores = int(input("Forneça a quantidade de eleitores: "))
if nEleitores < 3:
    print("A quantidade de eleitores é inferior a 3")
    nEleitores = int(input("Forneça a quantidade de eleitores: "))
else:
    print("## Votação Iniciada")
    for i in range(nEleitores):
        voto = int(input("Forneça o número do candidato que deseja votar: "))
        if voto == n1:
            n1Quantidade = n1Quantidade + 1
        elif voto == n2:
            n2Quantidade = n2Quantidade + 1
        else:
            nInvalido = nInvalido + 1
    print("## Votação Encerrada")

votosValidos = n1Quantidade + n2Quantidade

print(f"Votos válidos: {(votosValidos / 100):.2f}% ({votosValidos} votos)")
print(f"Votos inválidos: {(nInvalido / 100):.2f}% ({nInvalido} votos)")
print(f"Votos para {candidato1}: {(n1Quantidade / 100):.2f}%")
print(f"Votos para {candidato2}: {(n2Quantidade / 100):.2f}%")
    
    
    