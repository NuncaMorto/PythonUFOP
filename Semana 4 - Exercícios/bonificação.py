pfuncionario = float(input("Informe a pontuação: "))

if (pfuncionario < 0) or (pfuncionario > 10):
    print("Pontuação inválida!")
else:
    salario = float(input("Informe o salário: "))
    if pfuncionario <= 3:
        bonificacao = 0
        print("Bonificação: 0%")
        print(f"Valor da bonificação: R$ {bonificacao:.2f}")
        print(f"Salário total: R$ {salario:.2f}")
    elif pfuncionario > 3 and pfuncionario <= 6:
        bonificacao = salario * 0.05
        print("Bonificação: 5%")
        print(f"Valor da bonificação: R$ {bonificacao:.2f}")
        print(f"Salário total: R$ {(salario + bonificacao):.2f}")
    elif pfuncionario > 6 and pfuncionario <= 8:
        bonificacao = salario * 0.1
        print("Bonificação: 10%")
        print(f"Valor da bonificação: R$ {bonificacao:.2f}")
        print(f"Salário total: R$ {(salario + bonificacao):.2f}")
    elif pfuncionario > 8:
        bonificacao = salario * 0.2
        print("Bonificação: 20%")
        print(f"Valor da bonificação: R$ {bonificacao:.2f}")
        print(f"Salário total: R$ {(salario + bonificacao):.2f}")
