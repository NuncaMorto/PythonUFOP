tempoT = int(input("Digite o tempo para a evacuação: "))
capacidade = int(input("Digite a capacidade de evacuação: "))
pessoasQ = int(input("Digite a quantidade de pessoas: "))

for i in range(tempoT):
    if capacidade <= pessoasQ:
        print(f"Explosão em {tempoT - i} segundos. Pessoas evacuadas: {capacidade}")
    capacidade += capacidade

if capacidade == pessoasQ:
    print(f"Explosão! Sucesso: evacuação completa!")
else:
    print(f"Explosão! Falha: faltaram {capacidade - pessoasQ} pessoas para evacuar!")
