c = float(input("Informe o capital emprestado: "))
m = int(input("Informe a quantidade de meses para quitação: "))

if c <= 10000: 
    t = 0.1
    j = c * m * t

    print("Taxa de juros aplicada: 10%")
    print(f"Juros devido: {j:.2f}")
    print(f"Valor total:{(c+j):.2f}")
else: 
    t = 0.07
    j = c * m * t
    print("Taxa de juros aplicada: 7%")
    print(f"Juros devido: {j:.2f}")
    print(f"Valor total:{(c+j):.2f}")
