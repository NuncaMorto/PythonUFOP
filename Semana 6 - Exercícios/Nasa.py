tempoT = int(input("Digite o tempo para a evacuação: "))
capacidadeT = int(input("Digite a capacidade de evacuação: "))
pessoasQ = int(input("Digite a quantidade de pessoas: "))

print("")

capacidade = 0

for i in range(tempoT, 0, -1):
    capacidade += capacidadeT
    if capacidade >= pessoasQ:
        capacidade = pessoasQ
    print(f"Explosão em {i} segundos. Pessoas evacuadas: {capacidade}")

print("")

if capacidade >= pessoasQ:
    print(f"Explosão! Sucesso: evacuação completa!")
else:
    print(f"Explosão! Falha: faltaram {pessoasQ - capacidade} pessoas para evacuar!")