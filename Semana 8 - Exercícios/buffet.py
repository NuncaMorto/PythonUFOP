def ValorProporcional(Q, P):
    V = Q * P / 100
    return V 

quantM = int(input("Informe a quantidade de mulheres: "))
quantH = int(input("Informe a quantidade de homens: "))

total = quantM + quantH

pMulheres = ValorProporcional(quantM, 20)
pHomens = ValorProporcional(quantH, 10)

totalVeg = pMulheres + pHomens

print(f"{pMulheres:.0f} alunas preferem refeição vegetariana.")
print(f"{pHomens:.0f} alunos preferem refeição vegetariana.")

print(f"A porcentagem de estudantes que preferem refeição vegetariana é {(totalVeg / total * 100):.1f}%.")
