peso = float(input("Digite seu peso (em kg): "))
altura = float(input("Digite sua altura (em metros): "))
sexo = str(input("Seu sexo é masculino (M) ou feminino (F)? "))

imc = peso/(altura**2)

if sexo == "M": 
    if imc <= 25:
        print("Você não precisa perder peso para ter IMC <= 25")
    else:
        peso2 = 25 * (altura**2)
        print(f"Você deve perder {(peso - peso2):.2f}kg para ter IMC = 25")
elif sexo == "F":
    if imc <= 24:
        print("Você não precisa perder peso para ter IMC <= 24")
    else:
        peso2 = 24 * (altura**2)
        print(f"Você deve perder {(peso - peso2):.2f}kg para ter IMC = 24")
else:
    print("A entrada contém dados não reconhecidos")

