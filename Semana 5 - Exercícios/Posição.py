iPosition = float(input("Informe a posição inicial (Si): "))
while iPosition < 0:
    iPosition = float(input("Informe a posição inicial (Si): "))
vel = float(input("Informe a velocidade (v): "))
while vel <= 0:
    vel = float(input("Informe a velocidade (v): "))
time = float(input("Informe o instante de tempo (t): "))
while time <= 0:
    time = float(input("Informe o instante de tempo (t): "))
S = iPosition + vel * time
print(f"A posição final no tempo t = {time:.2f} será S = {S:.2f}")