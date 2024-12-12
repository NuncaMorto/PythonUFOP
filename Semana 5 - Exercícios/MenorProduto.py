produto = str(input("Digite o nome do produto: "))
quantidade = int(input("Digite a quantidade de unidades vendidas: "))

menorP = produto
menorQ = quantidade

while produto != "":
    if quantidade < menorQ:
        menorQ = quantidade
        menorP = produto
    produto = str(input("Digite o nome do produto: "))
    if produto != "":
        quantidade = int(input("Digite a quantidade de unidades vendidas: "))
       
print(f"Produto com menor venda: {menorP} ({menorQ} unidades)")

    