time1 = int(input("Digite o placar do primerio time: "))
time2 = int(input("Digite o placar do segundo time: "))

if  time1 < time2:
    print("O time 2 ganhou!!")
elif time1 > time2:
    print("O time 1 ganhou!!")
else:
    print("Empate")