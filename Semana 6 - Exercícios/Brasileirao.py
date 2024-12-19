nJuiz = str(input("Informe o nome do juiz: "))
nPartidas = int(input("Informe a quantidade de partidas: "))

n = 0
impedimento = 0 
faltas = 0 
cartoes = 0
acrescimos = 0

for i in range(nPartidas, 0, -1):
    n += 1
    print(f"Partida {n}:")
    impedimento += int(input(". Informe impedimentos.......: ")) 
    faltas += int(input(". Informe faltas.............: "))
    cartoes += int(input(". Informe cartões............: ")) 
    acrescimos += float(input(". Informe tempo de acréscimo.: "))

print(f"Estatísticas do juiz {nJuiz}: ")
print(f". Impedimentos.......: {(impedimento / n):.2f}")
print(f". Faltas.............: {(faltas / n):.2f}")
print(f". Cartões............: {(cartoes / n):.2f}")
print(f". Tempo de acréscimo.: {(acrescimos / n):.2f}")
