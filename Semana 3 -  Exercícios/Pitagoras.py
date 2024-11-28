a = int(input("Informe o cateto 1 (a): "))
b = int(input("Informe o cateto 2 (b): "))
c = int(input("Informe a hipotenusa (c): "))

if (a**2 + b**2) == c**2: 
    print(f"{a}, {b}, {c} representam um terno pitagórico")
else:
    print(f"{a}, {b}, {c} NÃO representam um terno pitagórico")