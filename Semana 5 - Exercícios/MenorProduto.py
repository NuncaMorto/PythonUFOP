produto = input("Digite o nome do produto: ")
quant = int(input("Digite a quantidade de unidades vendidas: "))

menorP = produto
menorQ = quantidade

while produto != "":
    produto = str(input("Digite o nome do produto: "))
    quant = int(input("Digite a quantidade de unidades vendidas: "))
    if quant < menorQ: 
        menorQ = quant
        menorP = produto 
print(f"Produto com menor venda: {menorP} ({menorQ} unidades)")

    