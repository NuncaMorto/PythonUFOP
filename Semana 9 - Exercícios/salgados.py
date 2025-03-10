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

def calculaLucros(vendasCoxinhas, vendasQuibes, lucroCoxinha, lucroQuibe):
    lucros = []
    for i in range(len(vendasCoxinhas)):
        lucro = vendasCoxinhas[i] * lucroCoxinha + vendasQuibes[i] * lucroQuibe
        lucros.append(round(lucro, 2))
    return lucros

def main():
    vendasCoxinhas = inputVetor("Informe as vendas de coxinhas: ", int)
    vendasQuibes = inputVetor("Informe as vendas de quibes: ", int)
    
    if len(vendasCoxinhas) != len(vendasQuibes):
        print("Dados de vendas inválidos")
        return
    
    lucroCoxinha = float(input("Informe o lucro por unidade de coxinha: R$ "))
    lucroQuibe = float(input("Informe o lucro por unidade de quibe: R$ "))
    
    lucros = calculaLucros(vendasCoxinhas, vendasQuibes, lucroCoxinha, lucroQuibe)
    
    print(f"Lucros: {lucros}")
    print(f"Maior lucro: R$ {max(lucros):.2f}")
    print(f"Menor lucro: R$ {min(lucros):.2f}")

if __name__ == "__main__":
    main()

