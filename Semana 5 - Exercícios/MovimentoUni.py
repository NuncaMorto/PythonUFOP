iPosition = int(input("Informe a posição inicial (Si): "))
while iPosition < 0:
    iPosition = int(input("Informe a posição inicial (Si): "))

vel = int(input("Informe a velocidade (v): "))
while vel <= 0:
    vel = int(input("Informe a velocidade (v): "))
 
tempo = int(input("Informe o instante de tempo (t): "))
while tempo <= 0: 
    tempo = int(input("Informe o instante de tempo (t): "))

print(f"A posição final no tempo t = {tempo:.2f} será S = {S = iPosition + vel * tempo}")
