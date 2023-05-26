num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))
tipo = int(input("Digite o tipo de conta que deseja: (1-Soma, 2-Subtração, 3-Multiplicação, 4-Divisão): "))

if tipo == 1:
    print("Resultado:", num1 + num2)
elif tipo == 2:
    print("Resultado:", num1 - num2)
elif tipo == 3:
    print("Resultado:", num1 * num2)
elif tipo == 4:
    print("Resultado:", num1 / num2)
