produto = str(input("Digite o nome do produto: "))
quant = int(input("Digite a quantidade de unidades vendidas: "))

menorP = produto
menorQ = quant

while len(produto) > 0:
    produto = str(input("Digite o nome do produto: "))
    quant = int(input("Digite a quantidade de unidades vendidas: "))
    if quant < menorQ: 
        menorQ = quant
        menorP = produto 
print(f"Produto com menor venda: {menorP} ({menorP} unidades)")

    