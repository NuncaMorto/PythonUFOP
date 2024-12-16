vendas = float(input("Digite o valor da venda: "))
total = vendas
while vendas > 0:
    vendas = float(input("Digite o valor da venda: "))
    if vendas > 0:
        total += vendas
    
print("")
print(f"Total de vendas: R$ {total:.2f}")