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

def getDivisores(n):
    divisores = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisores.append(i)
    return divisores

def isPrimo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def main():
    numeros = inputVetor("Digite os números: ", int)
    
    if not numeros:
        print("Nenhum número informado")
        return
    
    for numero in numeros:
        if isPrimo(numero):
            print(f"{numero} é um número primo.")
        else:
            divisores = getDivisores(numero)
            print(f"{numero} não é um número primo.")
            print("Seus divisores são:")
            print(divisores)
            print("")

if __name__ == "__main__":
    main()